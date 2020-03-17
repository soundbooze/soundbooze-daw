syntax on
set number
set ruler
set ai
set ic
set ts=2
set sw=2
set expandtab
set nowrap
set noswapfile
color jellybeans
set guifont=Monospace\ 11
"set autochdir

":set guioptions-=m  "remove menu bar
:set guioptions-=T  "remove toolbar
:set guioptions-=r  "remove right-hand scroll bar
:set guioptions-=L  "remove left-hand scroll bar

set rtp+=~/.vim/bundle/Vundle.vim

call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
Plugin 'itchyny/lightline.vim'
Plugin 'scrooloose/nerdtree'
"Plugin 'Valloric/YouCompleteMe'

let g:ycm_global_ycm_extra_conf="~/.vim/bundle/YouCompleteMe/third_party/ycmd/ycmd/tests/clang/testdata/.ycm_extra_conf.py"

call vundle#end()

filetype plugin indent on

" Enable Tlist toggle with F8
nnoremap <silent> <F8> :TlistToggle<CR>
map <C-o> :NERDTreeToggle<CR>

" cflow
command! -complete=shellcmd -nargs=+ Shell call s:RunShellCommand(<q-args>)
function! s:RunShellCommand(cmdline)
  let isfirst = 1
  let words = []
  for word in split(a:cmdline)
    if isfirst
      let isfirst = 0  " don't change first word (shell command)
    else
      if word[0] =~ '\v[%#<]'
        let word = expand(word)
      endif
      let word = shellescape(word, 1)
    endif
    call add(words, word)
  endfor
  let expanded_cmdline = join(words) . ' ' . shellescape(expand('%:p'), 1)
  botright vnew
  setlocal buftype=nofile bufhidden=wipe nobuflisted noswapfile nowrap filetype=c
  call setline(1, 'You entered:  ' . a:cmdline)
  call setline(2, 'Expanded to:  ' . expanded_cmdline)
  call append(line('$'), substitute(getline(2), '.', '=', 'g'))
  silent execute '$read !'. expanded_cmdline
  1
endfunction

let g:cflow="off"
function! ToggleCflow()
  if g:cflow == "on"
    let g:cflow="off"
    pclose
  else
    let g:cflow="on"
    :Shell cflow -Tn 
  endif
endfunction

nnoremap <F5> :call ToggleCflow()<CR>

autocmd BufEnter *.vue :setlocal filetype=html
