
import requests
import speedtest
import json
import time
import os
import yaml # Import the yaml library

def get_current_public_ip():
    """
    Gets the current public IP address.
    获取当前公共 IP 地址。
    """
    try:
        response = requests.get('https://api.ipify.org?format=json', timeout=5)
        response.raise_for_status()  # Check if the HTTP request was successful 检查 HTTP 请求是否成功
        return response.json()['ip']
    except requests.exceptions.RequestException as e:
        print(f"Error getting public IP: {e}")
        return None

def get_ip_location(ip_address):
    """
    Uses ip-api.com to get geographical location information for an IP address.
    Free version limit: 45 requests per minute.
    使用 ip-api.com 获取 IP 地址的地理位置信息。
    免费版限制：每分钟 45 次请求。
    """
    try:
        # Request additional fields 'status' and 'message' for better error handling
        # 请求额外的 'status' 和 'message' 字段，以便更好地处理错误
        response = requests.get(f'http://ip-api.com/json/{ip_address}?fields=country,city,regionName,isp,lat,lon,status,message', timeout=5)
        response.raise_for_status()
        data = response.json()
        if data and data.get('status') == 'success':
            country = data.get('country', '未知国家')
            city = data.get('city', '未知城市')
            region = data.get('regionName', '未知地区')
            isp = data.get('isp', '未知ISP')
            return f"{country}, {region}, {city} ({isp})"
        else:
            # If status is not 'success', print the full response for debugging
            # 如果状态不是 'success'，打印完整响应以进行调试
            print(f"  IP-API response indicates failure: {json.dumps(data, ensure_ascii=False)}")
            message = data.get('message', '未知错误')
            return f"IP Location Failed: {message}"
    except requests.exceptions.RequestException as e:
        return f"IP Location Error: {e}"

def run_speed_test():
    """
    Performs a speed test using speedtest-cli.
    Returns download speed (Mbps), upload speed (Mbps), latency (ms).
    使用 speedtest-cli 进行速度测试。
    返回下载速度 (Mbps), 上传速度 (Mbps), 延迟 (ms)。
    """
    try:
        st = speedtest.Speedtest()
        print("Finding best server for speed test... 正在寻找最佳测速服务器...")
        st.get_best_server()
        server_info = st.results.server
        print(f"Testing download speed (server: {server_info.get('sponsor', 'Unknown')} - {server_info.get('name', 'Unknown')})... 正在测试下载速度...")
        download_speed = st.download()
        print("Testing upload speed... 正在测试上传速度...")
        upload_speed = st.upload()
        latency = st.results.ping

        # Convert to Mbps 转换为 Mbps
        download_speed_mbps = download_speed / 1_000_000
        upload_speed_mbps = upload_speed / 1_000_000
        
        return download_speed_mbps, upload_speed_mbps, latency
    except speedtest.SpeedtestException as e:
        print(f"Speed test error: {e}")
        return None, None, None
    except Exception as e:
        print(f"An unexpected error occurred during speed test: {e}")
        return None, None, None

def process_vpn_config(yaml_config_string, output_file="updated_config.yaml"):
    """
    Parses a YAML configuration string, processes VPN proxies within it
    by adding speed and region information to their names, and saves
    the updated configuration to a new YAML file. It also updates
    proxy names in 'proxy-groups' accordingly.
    解析 YAML 配置字符串，处理其中的 VPN 代理，通过在名称中添加速度和地区信息，
    并将更新后的配置保存到新的 YAML 文件。它还会相应地更新 'proxy-groups' 中的代理名称。

    :param yaml_config_string: The input YAML configuration as a string.
    :param output_file: The name of the output YAML file.
    """
    try:
        # Load the YAML configuration
        # 加载 YAML 配置
        config = yaml.safe_load(yaml_config_string)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML config: {e}")
        print(f"解析 YAML 配置时出错: {e}")
        return

    if 'proxies' not in config or not isinstance(config['proxies'], list):
        print("Error: 'proxies' section not found or is not a list in the YAML config.")
        print("错误：YAML 配置中未找到 'proxies' 部分或它不是一个列表。")
        return

    proxies = config['proxies']
    
    print("\n--- Starting VPN Proxy Information Collection ---")
    print("--- 正在开始收集 VPN 代理信息 ---")
    print("Please ensure you manually connect to each VPN proxy's server before running its test.")
    print("请确保在运行每个代理的测试之前，手动连接到该 VPN 代理的服务器。")

    # This dictionary will map original proxy names to their new, updated names
    # 这个字典将映射原始代理名称到其新的、更新后的名称
    name_mapping = {}

    # Iterate through the proxies directly within the loaded config
    # 直接在已加载的配置中遍历代理
    for i, proxy in enumerate(proxies):
        original_name = proxy.get('name', f"Proxy {i+1}")
        # The 'server' field might be an IP or a domain, use it to guide the user
        # 'server' 字段可能是一个 IP 或域名，用于指导用户
        server_for_user_guide = proxy.get('server', 'Unknown Server')

        print(f"\nProcessing proxy: {original_name} (Server: {server_for_user_guide})")
        print(f"正在处理代理：{original_name} (服务器: {server_for_user_guide})")
        print(f"  (Please connect to '{original_name}' (via {server_for_user_guide}) on your VPN client NOW and press Enter to continue.)")
        print(f"  (请立即在您的 VPN 客户端上连接到 '{original_name}' (通过 {server_for_user_guide}) 并按 Enter 键继续。)")
        input("  Press Enter when connected... 连接后请按 Enter 键...")

        current_public_ip = get_current_public_ip()
        if not current_public_ip:
            print(f"  Could not get public IP for {original_name}. Skipping this proxy.")
            print(f"  无法获取 {original_name} 的公共 IP。跳过此代理。")
            # If skipping, we still update the proxy entry to include any existing data,
            # but we don't modify its name or add speed info.
            # 如果跳过，我们仍然更新代理条目以包含任何现有数据，
            # 但我们不修改其名称或添加速度信息。
            proxy['resolved_ip'] = "Failed to get IP"
            proxy['region_info'] = "Failed to get location"
            # Add to mapping even if skipped, to ensure proxy groups don't break,
            # but map to original name if no update occurred.
            # 即使跳过也添加到映射中，以确保代理组不会中断，
            # 但如果未发生更新，则映射到原始名称。
            name_mapping[original_name] = original_name
            continue

        print(f"  Current public IP detected: {current_public_ip}")
        print(f"  检测到当前公共 IP: {current_public_ip}")

        # Get region information based on the current public IP
        # 根据当前公共 IP 获取地区信息
        region_name = get_ip_location(current_public_ip)
        print(f"  Region: {region_name}")
        print(f"  地区: {region_name}")

        # Perform speed test
        # 进行速度测试
        download, upload, latency = run_speed_test()

        if download is not None and upload is not None and latency is not None:
            new_name = f"{original_name} - {region_name} - 下载: {download:.2f} Mbps, 上传: {upload:.2f} Mbps, 延迟: {latency:.2f} ms"
            
            # Update the name in the proxy dictionary
            # 更新代理字典中的名称
            proxy['name'] = new_name
            
            # Store the mapping from original name to new name
            # 存储从原始名称到新名称的映射
            name_mapping[original_name] = new_name

            # Add additional info to the proxy dictionary for detailed tracking
            # 将附加信息添加到代理字典中以进行详细跟踪
            proxy['resolved_ip'] = current_public_ip # The actual IP detected
            proxy['region_info'] = region_name
            proxy['download_speed_mbps'] = round(download, 2)
            proxy['upload_speed_mbps'] = round(upload, 2)
            proxy['latency_ms'] = round(latency, 2)
            print(f"  Updated name: {new_name}")
            print(f"  更新后的名称: {new_name}")
        else:
            print(f"  Failed to get speed test results for {original_name}. Keeping original name but adding IP/Region if available.")
            print(f"  未能获取 {original_name} 的速度测试结果。保留原始名称，但添加 IP/地区（如果可用）。")
            proxy['resolved_ip'] = current_public_ip
            proxy['region_info'] = region_name
            # If speed test failed, map to original name
            # 如果速度测试失败，则映射到原始名称
            name_mapping[original_name] = original_name
            # Do not update speed fields if test failed 不更新速度字段，如果测试失败

        print("  Waiting for 5 seconds before next proxy to avoid API rate limits... 等待 5 秒钟以避免 API 速率限制...")
        time.sleep(5)

    # --- Update proxy names in proxy-groups ---
    # --- 更新 proxy-groups 中的代理名称 ---
    if 'proxy-groups' in config and isinstance(config['proxy-groups'], list):
        print("\n--- Updating proxy names in proxy-groups ---")
        print("--- 正在更新 proxy-groups 中的代理名称 ---")
        for group in config['proxy-groups']:
            if 'proxies' in group and isinstance(group['proxies'], list):
                updated_group_proxies = []
                for old_proxy_name in group['proxies']:
                    # Check if the proxy name is one that we processed and updated
                    # 检查代理名称是否是我们处理并更新过的名称
                    if old_proxy_name in name_mapping:
                        updated_group_proxies.append(name_mapping[old_proxy_name])
                    else:
                        # If it's not a name we processed (e.g., 'DIRECT'), keep it as is
                        # 如果它不是我们处理过的名称（例如 'DIRECT'），则保持原样
                        updated_group_proxies.append(old_proxy_name)
                group['proxies'] = updated_group_proxies
                print(f"  Updated group '{group.get('name', 'Unknown Group')}': {group['proxies']}")
                print(f"  已更新组 '{group.get('name', '未知组')}': {group['proxies']}")

    try:
        # Save the entire modified configuration to a new YAML file
        # 将整个修改后的配置保存到新的 YAML 文件
        with open(output_file, 'w', encoding='utf-8') as f:
            # Use safe_dump for security and readability
            # indent=2 for standard YAML formatting, allow_unicode=True for Chinese characters
            # sort_keys=False to preserve the original order of keys
            # 使用 safe_dump 进行安全性和可读性，indent=2 为标准 YAML 格式，allow_unicode=True 支持中文，sort_keys=False 保持原始键顺序
            yaml.safe_dump(config, f, indent=2, allow_unicode=True, sort_keys=False)
        print(f"\n--- Processing complete. Updated config saved to {output_file} ---")
        print(f"--- 处理完成。更新后的配置已保存到 {output_file} ---")
    except Exception as e:
        print(f"Error saving updated config to file: {e}")
        print(f"保存更新后的配置到文件时出错: {e}")

# --- Main program entry --- 主程序入口 ---
if __name__ == "__main__":
    # Prompt the user for the YAML config file path
    # 提示用户输入 YAML 配置文件路径
    yaml_file_path = input("请输入您的 YAML 配置文件的路径 (例如: config.yaml): ")
    
    # Check if the file exists
    # 检查文件是否存在
    if not os.path.exists(yaml_file_path):
        print(f"错误: 文件 '{yaml_file_path}' 不存在。请提供一个有效的文件路径。")
    else:
        try:
            # Read the YAML config from the specified file
            # 从指定文件中读取 YAML 配置
            with open(yaml_file_path, 'r', encoding='utf-8') as f:
                user_yaml_config = f.read()
            
            # Process the YAML configuration and save to 'updated_config.yaml'
            # 处理 YAML 配置并保存到 'updated_config.yaml'
            process_vpn_config(user_yaml_config, output_file="updated_config.yaml")

        except Exception as e:
            print(f"读取或处理文件时发生错误 '{yaml_file_path}': {e}")

