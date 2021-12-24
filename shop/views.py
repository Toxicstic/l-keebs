from django.shortcuts import render

exampleListing = {
    'name'          :'Durock Sunflower POM t1 Switches',
    'description'   :'very tactile switches, nice quality',
    'price'         :'15'
}

# Create your views here.
def shop(request):
    context= {'exampleListing': exampleListing}
    return render(request, 'shop.html/',context)