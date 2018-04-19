from fuzzywuzzy import process

cities = ['Karachi', 'Lahore', 'Islamabad', 'Rawalpindi', 'Quetta', 'Peshawar', 'Gawadar', 'Multan', 'Hyderabad', 'Faisalabad'
          , 'Gujranwala', 'Rahim Yar Khan']

# limit = 3

result = process.extract('hk', cities, limit=3)

print(result)
