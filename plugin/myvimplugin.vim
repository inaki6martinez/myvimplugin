"-(functions) If last char is "," then the indent must be changed:
"      -Same tabs as "current" line
"      -If "current" line has "(", spaces until it
"      -
"-(inside conditionals (if, while...)) If brackets are opened:
"      - Spaces until "("
"-(#defines) if "\" is found:   
"      - Spaces until 
" When "o" is introduced as well

let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

python3 << EOF
import sys
from os.path import normpath, join
import vim
plugin_root_dir = vim.eval('s:plugin_root_dir')
python_root_dir = normpath(join(plugin_root_dir, '..', 'python'))
sys.path.insert(0, python_root_dir)
import sample
EOF

function! Indexation()
	python3 sample.print_country()
	echo changeIndex
	if changeIndex
		normal jA
	else
		normal o
	endif

endfunction
command! -nargs=0 Indexation call Indexation()

"inoremap <silent> <CR>  <ESC>:Indexation<CR>

