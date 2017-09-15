execute pathogen#infect()

syntax on
set bg=dark
set t_Co=256

set binary
set noeol
set number
set ts=4
set expandtab
set shiftwidth=4
set cursorline
set autoindent

au BufNewFile *.py r ~/.vim/template.py

" enable beep
set novisualbell

" show the matching part of the pair for [] {} and ()
set showmatch
set matchtime=0



" syntactic
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0

set laststatus=2
python from powerline.vim import setup as powerline_setup
python powerline_setup()
python del powerline_setup

" tarbar
nmap <F8> :TagbarToggle<CR>

autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif

"Nerdtree
"autocmd VimEnter * NERDTree
"autocmd VimEnter * wincmd p
map <C-n> :NERDTreeToggle<CR>

" jedi
autocmd FileType python setlocal completeopt-=preview

colorscheme monokai
let g:molokai_original = 1
let g:rehash256 = 1
" highlight Normal ctermfg=grey ctermbg=darkblue

"auto format
noremap <F3> :Autoformat<CR>

" Easy motion
map ,, <Plug>(easymotion-prefix)

let python_highlight_all = 1

" display shell command output in another window
function! s:ExecuteInShell(command)
   let command = join(map(split(a:command), 'expand(v:val)'))
   let winnr = bufwinnr('^' . command . '$')
   silent! execute  winnr < 0 ? 'botright new ' . fnameescape(command) : winnr . 'wincmd w'
   setlocal buftype=nowrite bufhidden=wipe nobuflisted noswapfile nowrap number
   echo 'Execute ' . command . '...'
   silent! execute 'silent %!'. command
   silent! execute 'resize ' . line('$')
   silent! redraw
   silent! execute 'au BufUnload <buffer> execute bufwinnr(' . bufnr('#') . ') . ''wincmd w'''
   silent! execute 'nnoremap <silent> <buffer> <LocalLeader>r :call <SID>ExecuteInShell(''' . command . ''')<CR>'
   echo 'Shell command ' . command . ' executed.'
endfunction

command! -complete=shellcmd -nargs=+ Shell call s:ExecuteInShell(<q-args>)
ca shell Shell

