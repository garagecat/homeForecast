homeForecast
=

Programme météo utilisant une sonde DHT22.
Un cron lance la mesure toutes les 15 minutes

*/15 *  * * * python /home/pi/Documents/homeForecast/homeForecast.py

On utilise plotly pour générer le graph dans /var/www/html/homeForecast.html
