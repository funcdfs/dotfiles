-- load options
require("options")

-- load keymappings
require("keymaps")

-- load plugins
require("plugins")

-- Set colorscheme
require("colors")

-- Set LSP
-- require("lsp")

if vim.g.neovide then
    -- Put anything you want to happen only in Neovide 
    vim.o.guifont = "Source Code Pro:h14" -- text below applies for VimScript
    vim.g.neovide_scroll_animation_length = 0.2
    vim.g.neovide_cursor_trail_size = 0.3
    vim.g.neovide_cursor_animation_length = 0.15
    vim.g.neovide_window_blurred = true
    vim.g.neovide_confirm_quit = true
    vim.g.neovide_remember_window_size = true
    vim.g.neovide_cursor_vfx_mode = "pixiedust"
    vim.g.neovide_cursor_vfx_particle_density = 1.2
    vim.g.neovide_opacity = 0.7
    vim.keymap.set('n', '<D-s>', ':w<CR>') -- Save
    vim.keymap.set('v', '<D-c>', '"+y') -- Copy
    vim.keymap.set('n', '<D-v>', '"+P') -- Paste normal mode
    vim.keymap.set('v', '<D-v>', '"+P') -- Paste visual mode
    vim.keymap.set('c', '<D-v>', '<C-R>+') -- Paste command mode
    vim.keymap.set('i', '<D-v>', '<ESC>l"+Pli') -- Paste insert mode
end


-- Allow clipboard copy paste in neovim
vim.api.nvim_set_keymap('', '<D-v>', '+p<CR>', { noremap = true, silent = true})
vim.api.nvim_set_keymap('!', '<D-v>', '<C-R>+', { noremap = true, silent = true})
vim.api.nvim_set_keymap('t', '<D-v>', '<C-R>+', { noremap = true, silent = true})
vim.api.nvim_set_keymap('v', '<D-v>', '<C-R>+', { noremap = true, silent = true})


vim.o.cursorline = true -- Ensure the cursorline is enabled
-- vim.cmd([[
--   highlight CursorLine guibg=#000000 guifg=FFFFFF
-- ]])