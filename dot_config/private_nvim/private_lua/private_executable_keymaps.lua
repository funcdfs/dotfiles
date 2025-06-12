-- define common options
local opts = {
    noremap = true,      -- non-recursive
    silent = true,       -- do not show message
}

local bind = vim.keymap.set
local opts = { noremap = true, silent = true }


-- F 相关，没有 touchbar 的时候再说。

-- 保存到剪贴板
-- vim.api.nvim_set_keymap('n', '<F1>', ':w !clip.exe<CR>', { noremap = true, silent = true })

-- 切换显示行号
-- vim.api.nvim_set_keymap('n', '<F2>', ':set nu! nu?<CR>', { noremap = true, silent = true })

-- 切换显示不可见字符
-- vim.api.nvim_set_keymap('n', '<F3>', ':set list! list?<CR>', { noremap = true, silent = true })

-- 切换自动换行
-- vim.api.nvim_set_keymap('n', '<F4>', ':set wrap! wrap?<CR>', { noremap = true, silent = true })

-- 离开插入模式时自动关闭 paste 模式
vim.cmd([[
  autocmd InsertLeave * set nopaste
]])

-- 切换语法高亮
-- vim.api.nvim_set_keymap('n', '<F6>', ":lua if vim.fn.exists('syntax_on') == 1 then vim.cmd('syntax off') else vim.cmd('syntax on') end<CR>", { noremap = true, silent = true })

-- 保存到剪贴板并执行多次回车
-- vim.api.nvim_set_keymap('n', '<F7>', ':w !clip.exe<CR><CR>', { noremap = true, silent = true })

-- leader key is '\'
vim.g.mapleader = '\\'

-- Quickly close the current window
vim.api.nvim_set_keymap('n', '<leader>q', ':q<CR>', { noremap = true, silent = true })

-- Quickly save the current file
vim.api.nvim_set_keymap('n', '<leader>w', ':w<CR>', { noremap = true, silent = true })

-- Quickly delete all content
vim.api.nvim_set_keymap('n', '<Leader>d', 'ggdG', { noremap = true, silent = true })

-- When in Normal Mode, quickly copy all content to system clipboard
vim.api.nvim_set_keymap('n', '<Leader>c', 'ggVG"+y', { noremap = true, silent = true })

-- When in Visual Mode, quickly copy selected content to system clipboard
vim.api.nvim_set_keymap('v', '<leader>c', '"+y', { noremap = true, silent = true })



-- 'kj' 作为 Esc 键
vim.api.nvim_set_keymap('i', 'kj', '<Esc>', {noremap = true, nowait = true})
vim.o.timeoutlen = 200

-- 方括号跳转
vim.api.nvim_set_keymap('n', '<TAB>', '%', { noremap = true, silent = true })

-- 重做命令
vim.api.nvim_set_keymap('n', 'U', '<C-r>', { noremap = true, silent = true })

-- 移除高亮
vim.api.nvim_set_keymap('n', '<leader>/', ':nohls<CR>', { noremap = true, silent = true })

-- Shift+H 跳转到行头，Shift+L 跳转到行尾
vim.api.nvim_set_keymap('n', 'H', '^', { noremap = true, silent = true })
vim.api.nvim_set_keymap('n', 'L', '$', { noremap = true, silent = true })
-- In Visual mode
vim.api.nvim_set_keymap('v', 'H', '^', { noremap = true, silent = true })
vim.api.nvim_set_keymap('v', 'L', '$', { noremap = true, silent = true })
-- In Operator-pending mode
vim.api.nvim_set_keymap('o', 'H', '^', { noremap = true, silent = true })
vim.api.nvim_set_keymap('o', 'L', '$', { noremap = true, silent = true })
-- In Select mode
vim.api.nvim_set_keymap('x', 'H', '^', { noremap = true, silent = true })
vim.api.nvim_set_keymap('x', 'L', '$', { noremap = true, silent = true })

-- 在搜索时保持搜索模式在屏幕中央
vim.api.nvim_set_keymap('n', 'n', 'nzz', { noremap = true, silent = true })
vim.api.nvim_set_keymap('n', 'N', 'Nzz', { noremap = true, silent = true })
vim.api.nvim_set_keymap('n', '*', '*zz', { noremap = true, silent = true })
vim.api.nvim_set_keymap('n', '#', '#zz', { noremap = true, silent = true })
vim.api.nvim_set_keymap('n', 'g*', 'g*zz', { noremap = true, silent = true })

-- 缩进/反缩进后重新选中可视块
vim.api.nvim_set_keymap('v', '<', '<gv', { noremap = true, silent = true })
vim.api.nvim_set_keymap('v', '>', '>gv', { noremap = true, silent = true })

-- Y 操作行为类似其他大写字母命令
vim.api.nvim_set_keymap('n', 'Y', 'y$', { noremap = true, silent = true })

-- paste and indent
vim.keymap.set('n', '<Leader>v', 'i<C-r><C-o>+<ESC>l=`[`]$', { desc = 'Paste block and indent'})
