:imap jj <Esc> 
set number
set nocompatible
syntax on
set showcmd
set mouse=a
set encoding=utf-8
set softtabstop=4
set shiftwidth=4
set tabstop=4 " 设置空格缩进
set cursorline
set wrap
set incsearch
set ignorecase
set history=100
set autoread
set listchars=tab:»■,trail:■
func SetTitle()
call setline(1, "\#!/usr/bin/python")
call setline(2, "\# -*- coding=utf8 -*-")
call setline(3, "\"\"\"")
call setline(4, "\# @Author : pig")
call setline(5, "\# @CreatedTime:".strftime("%Y-%m-%d%H:%M:%S"))
call setline(6, "\# @Description : ")
call setline(7, "\"\"\"")
normal G
normal o
normal o
endfunc
autocmd bufnewfile *.py call SetTitle()
inoremap ' ''<Esc>i
inoremap " ""<Esc>i
inoremap ( ()<Esc>i
inoremap [ []<Esc>i
inoremap { {<CR>}<Esc>o


