from django.shortcuts import render

# Create your views here.
def index(request):
df = pd.read_csv(‘worldcities.csv’)
city = ‘Tokyo’
lat = df[df[‘city_ascii’] == city][‘lat’] lon = df[df[‘city_ascii’] == city][‘lng’]print(lat)
print(‘n’)
print(lon)
return render(request, ‘weather/index.html’)
