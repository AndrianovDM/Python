from user_interface import pressure_view
from user_interface import temperature_view
from user_interface import wind_speed_view

def create(device = 1):
    style = 'style="font-size:22px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html +='     <p {}>Temperature: {} C</p>\n'\
        .format(style, temperature_view(device))
    html +='     <p {}>Wind_speed: {} m</s</p>\n'\
        .format(style, wind_speed_view(device))
    html +='     <p {}>Pressure: {} mmHg</p>\n'\
        .format(style, pressure_view(device))
    html += '   </body>\n</html>'

    with open('C:\\Users\\Dmitry\\Downloads\\Postgraduate studies\\Homework program\\Python\\Lecture4\\sensor\\index.html','w', encoding = 'utf-8') as page:
        page.write(html)
    
    return html

def new_create(data, device = 1):
    t, p, w = data
    t = t*1.8 +32
    style = 'style="font-size:22px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html +='     <p {}>Temperature: {} F</p>\n'\
        .format(style, t)
    html +='     <p {}>Wind_speed: {} m</s</p>\n'\
        .format(style, w)
    html +='     <p {}>Pressure: {} mmHg</p>\n'\
        .format(style, p)
    html += '   </body>\n</html>'

    with open('C:\\Users\\Dmitry\\Downloads\\Postgraduate studies\\Homework program\\Python\\Lecture4\\sensor\\new_index.html','w', encoding = 'utf-8') as page:
        page.write(html)
    
    return data