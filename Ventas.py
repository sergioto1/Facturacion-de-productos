def Ventas(Categoria,Valor,Cantidad) :
    VentasProducto = list(map(lambda x,y :  x * y,Cantidad,Valor))
    sum=0
    for x in VentasProducto :
        sum+=x
   
    May = 0
    for x in VentasProducto :
        if x > May : 
            May = x

    for i in range(len(Cantidad)):
        if Cantidad[i] > 10 :
            Descuento = list(map(lambda x,y :  (x * y) * 0.10 ,Cantidad,Valor))
        else :
            Cantidad[i] = 0

        
    sum1=0
    for x in Descuento :
        sum1+=x
   
    print(f"Factura = {VentasProducto}")
    print(f"Descuento = {Descuento}")
    
    VentasTotales={}
    VentasTotales["Venta Total"] = int(sum - sum1)
    VentasTotales["Mayor venta"] = May
    return(VentasTotales)
