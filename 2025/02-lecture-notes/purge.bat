del *.log
del *.aux
del *.toc
del *.gz
del *.nav
del *.out
del *.snm
del *.ps
del *.vrb
for /d %%i in (_minted*) do rd "%%i"