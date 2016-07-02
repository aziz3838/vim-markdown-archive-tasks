" --------------------------------
" Add our plugin to the path
" --------------------------------
python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))

" --------------------------------
"  Ensure python support exists
" --------------------------------
if !has('python')
    finish
endif

" --------------------------------
"  Function(s)
" --------------------------------
function! MarkdownArchiveTasks()
python << endOfPython

from vim_markdown_archive_tasks import ArchiveTasks
ArchiveTasks().archive_tasks()

endOfPython
endfunction

" --------------------------------
"  Expose our commands to the user
" --------------------------------
command! ArchiveTasks call MarkdownArchiveTasks()
