pr_alcool, pr_gasol, quant_alcool, quant_gasol = map(float,input().split())

rend_alcool = quant_alcool/pr_alcool
rend_gasol = quant_gasol/pr_gasol

if (rend_gasol > rend_alcool or rend_alcool == rend_gasol):
    print("G")

else:
    print("A")