^t::
InputBox,time,kira专用计时器,

;弹出对话框

time := time * 1000
;和平常的表达式相比多了一个冒号

Sleep,%time%
;引用变量前后加%

MsgBox 时间到！
return