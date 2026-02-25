\d M
mar: "];"							/ 0: end loop
mAr: "p-:1;"						/ 1: dec mem ptr
maR: "p+:1;"						/ 2: inc mem ptr
mAR: ". M@(!M)@m p"				/ 3: eval
Mar: ".:[m p; M.OOM; M.oom];"	/ 4: read-write
MAr: "m[p]-:1;"					/ 5: dec mem
MaR: "m[p]+:1;"					/ 6: inc mem
MAR: "while[m p;"					/ 7: begin loop
mrr: "m[p]:0;"					/ 8: zero
MRR: ":[r~_n; r:m p; (r:_n;m[p]:r)];"	/ 9: save-load
Mrr: "`0:,$m p;"					/ 10: write
mrR: "m[p]:0$0:`;"				/ 11: read
\d ^
m:&10000; p:0; r:_n				/ set the stage
.,/M c@&(c:`$1_'(&c=*c)_ c:,/" ",/:0:_i 0)_lin!M / read, xlate, eval
\\


