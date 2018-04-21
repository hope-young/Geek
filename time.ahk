^t::
InputBox,time,kira's Timer,please input a time:
;弹出对话框

time := time * 1000
;和平常的表达式相比多了一个冒号

Sleep,%time%
;引用变量前后加%

MsgBox Time is up!!
return