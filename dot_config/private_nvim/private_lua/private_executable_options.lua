-- Hint: use `:h <option>` to figure out the meaning if needed
-- 提示：如果需要，可以使用`:h <选项>`来了解其含义

-- vim.opt.clipboard = "unnamedplus" -- use system clipboard
-- 将 Vim 的 clipboard（剪贴板）选项设置为"unnamedplus"，以便使用系统剪贴板。

vim.opt.completeopt = { "menu", "menuone", "noselect" }
-- 设置 Vim 的自动补全选项，包括显示补全菜单、仅显示一个补全项菜单以及不自动选择补全项。

vim.opt.mouse = "a" -- allow the mouse to be used in Nvim
-- 允许在 Neovim（Nvim）中使用鼠标。

vim.opt.scrolloff = 10 -- no less than 10 lines even if you keep scrolling down
-- 设置滚动偏移量为 10，即使不断向下滚动，也至少保留 10 行内容在屏幕上。

-- Tab
vim.opt.tabstop = 4 -- number of visual spaces per TAB
-- 设置一个制表符（TAB）在视觉上占用 4 个空格的宽度。

vim.opt.softtabstop = 4 -- number of spaces in tab when editing
-- 在编辑时，一个制表符等效于 4 个空格。

vim.opt.shiftwidth = 4 -- insert 4 spaces on a tab
-- 设置缩进宽度为 4 个空格，即按下制表符或进行缩进操作时插入 4 个空格。

vim.opt.expandtab = true -- tabs are spaces, mainly because of python
-- 将制表符扩展为空格，主要是为了适应 Python 等编程语言的缩进风格。

-- UI config
vim.opt.number = true -- show absolute number
-- 显示行号。

vim.opt.relativenumber = false -- add numbers to each line on the left side
-- 在每行左侧显示相对行号。

vim.opt.cursorline = true -- highlight cursor line underneath the cursor horizontally
-- 高亮显示光标所在行。

vim.opt.splitbelow = true -- open new vertical split bottom
-- 垂直分屏时，新窗口在下方打开。

vim.opt.splitright = true -- open new horizontal splits right
-- 水平分屏时，新窗口在右侧打开。

vim.opt.termguicolors = true -- enable 24-bit RGB color in the TUI
-- 在终端用户界面（TUI）中启用 24 位真彩色。

vim.opt.showmode = true -- we are experienced, wo don't need the "-- INSERT --" mode hint
-- 显示模式提示，例如“-- INSERT --”

-- Searching
vim.opt.incsearch = true -- search as characters are entered
-- 实时搜索，即随着输入字符立即进行搜索。

vim.opt.hlsearch = false -- do not highlight matches
-- 不高亮显示搜索结果。

vim.opt.ignorecase = true -- ignore case in searches by default
-- 默认情况下在搜索中忽略大小写。

vim.opt.smartcase = true -- but make it case sensitive if an uppercase is entered
-- 但如果输入了大写字母，则进行区分大小写的搜索。


-- 禁止创建备份文件
vim.o.backup = false
vim.o.writebackup = false
vim.o.swapfile = false