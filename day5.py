#day5 lists:
#1.
empty_list = [] #or empty_list = list()
#2.
list_5items = [1, 2, 3, 4, 5]
#3.
print(len(list_5items))
#4.
print(list_5items[::2])
#5.
mixed_data_types = [{
  "name": "Jeff",
  "age": 22,
}, 169, "Single", "Tulic, Argao, Cebu"]
#6.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
#7.
print(it_companies)
#8.
print(len(it_companies))
#9.
print(it_companies[::3])
#10.
it_companies[0] = 'FB'
print(it_companies)
#11.
it_companies.append('Kyocera')
#12.
it_companies.insert(4, 'Mid')
#13.
it_companies[1] = it_companies[1].upper()
print(it_companies)
#14.
# add = ['#;']
# it_companies += add
# print(it_companies)
#15.
print('Apple' in it_companies)
#16.
it_companies.sort()
print("SORT ASC: ", it_companies)
it_companies.sort(reverse=True)
print("SORT DESC: ", it_companies)
#17.
it_companies.reverse()
print('reverse: ', it_companies)
#18.
print(it_companies[:3])
#19.
print(it_companies[-3:])
#20.
mid = int(len(it_companies) / 2)
print(it_companies[mid])
#21.
print(it_companies.pop(0))#or .remove('text')
#22.
middle = it_companies[mid]
it_companies.remove(middle)
print(it_companies)
#23.
it_companies.pop()
print(it_companies)
#24.
it_companies.clear()
print(it_companies)
#25.
del it_companies
#26. & 27.
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)
#EXERCISE LEVEL 2:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min = ages[0]
max = ages[-1]
ages.append(min)
ages.append(max)
median = int(len(ages) / 2)
print(ages[median])
#average
# total = 0
# for item in ages:
#   total += item
# average = total / len(ages)
# print(average)
average = sum(ages) / len(ages)
print(average)
range = max-min
print(range)
print(abs(min-average) == (max-average))
#nation2:
# countries = [
#   'Afghanistan',
#   'Albania',
#   'Algeria',
#   'Andorra',
#   'Angola',
#   'Antigua and Barbuda',
#   'Argentina',
#   'Armenia',
#   'Australia',
#   'Austria',
#   'Azerbaijan',
#   'Bahamas',
#   'Bahrain',
#   'Bangladesh',
#   'Barbados',
#   'Belarus',
#   'Belgium',
#   'Belize',
#   'Benin',
#   'Bhutan',
#   'Bolivia',
#   'Bosnia and Herzegovina',
#   'Botswana',
#   'Brazil',
#   'Brunei',
#   'Bulgaria',
#   'Burkina Faso',
#   'Burundi',
#   'Cambodia',
#   'Cameroon',
#   'Canada',
#   'Cape Verde',
#   'Central African Republic',
#   'Chad',
#   'Chile',
#   'China',
#   'Colombi',
#   'Comoros',
#   'Congo (Brazzaville)',
#   'Congo',
#   'Costa Rica',
#   "Cote d'Ivoire",
#   'Croatia',
#   'Cuba',
#   'Cyprus',
#   'Czech Republic',
#   'Denmark',
#   'Djibouti',
#   'Dominica',
#   'Dominican Republic',
#   'East Timor (Timor Timur)',
#   'Ecuador',
#   'Egypt',
#   'El Salvador',
#   'Equatorial Guinea',
#   'Eritrea',
#   'Estonia',
#   'Ethiopia',
#   'Fiji',
#   'Finland',
#   'France',
#   'Gabon',
#   'Gambia, The',
#   'Georgia',
#   'Germany',
#   'Ghana',
#   'Greece',
#   'Grenada',
#   'Guatemala',
#   'Guinea',
#   'Guinea-Bissau',
#   'Guyana',
#   'Haiti',
#   'Honduras',
#   'Hungary',
#   'Iceland',
#   'India',
#   'Indonesia',
#   'Iran',
#   'Iraq',
#   'Ireland',
#   'Israel',
#   'Italy',
#   'Jamaica',
#   'Japan',
#   'Jordan',
#   'Kazakhstan',
#   'Kenya',
#   'Kiribati',
#   'Korea, North',
#   'Korea, South',
#   'Kuwait',
#   'Kyrgyzstan',
#   'Laos',
#   'Latvia',
#   'Lebanon',
#   'Lesotho',
#   'Liberia',
#   'Libya',
#   'Liechtenstein',
#   'Lithuania',
#   'Luxembourg',
#   'Macedonia',
#   'Madagascar',
#   'Malawi',
#   'Malaysia',
#   'Maldives',
#   'Mali',
#   'Malta',
#   'Marshall Islands',
#   'Mauritania',
#   'Mauritius',
#   'Mexico',
#   'Micronesia',
#   'Moldova',
#   'Monaco',
#   'Mongolia',
#   'Morocco',
#   'Mozambique',
#   'Myanmar',
#   'Namibia',
#   'Nauru',
#   'Nepal',
#   'Netherlands',
#   'New Zealand',
#   'Nicaragua',
#   'Niger',
#   'Nigeria',
#   'Norway',
#   'Oman',
#   'Pakistan',
#   'Palau',
#   'Panama',
#   'Papua New Guinea',
#   'Paraguay',
#   'Peru',
#   'Philippines',
#   'Poland',
#   'Portugal',
#   'Qatar',
#   'Romania',
#   'Russia',
#   'Rwanda',
#   'Saint Kitts and Nevis',
#   'Saint Lucia',
#   'Saint Vincent',
#   'Samoa',
#   'San Marino',
#   'Sao Tome and Principe',
#   'Saudi Arabia',
#   'Senegal',
#   'Serbia and Montenegro',
#   'Seychelles',
#   'Sierra Leone',
#   'Singapore',
#   'Slovakia',
#   'Slovenia',
#   'Solomon Islands',
#   'Somalia',
#   'South Africa',
#   'Spain',
#   'Sri Lanka',
#   'Sudan',
#   'Suriname',
#   'Swaziland',
#   'Sweden',
#   'Switzerland',
#   'Syria',
#   'Taiwan',
#   'Tajikistan',
#   'Tanzania',
#   'Thailand',
#   'Togo',
#   'Tonga',
#   'Trinidad and Tobago',
#   'Tunisia',
#   'Turkey',
#   'Turkmenistan',
#   'Tuvalu',
#   'Uganda',
#   'Ukraine',
#   'United Arab Emirates',
#   'United Kingdom',
#   'United States',
#   'Uruguay',
#   'Uzbekistan',
#   'Vanuatu',
#   'Vatican City',
#   'Venezuela',
#   'Vietnam',
#   'Yemen',
#   'Zambia',
#   'Zimbabwe',
# ]
import countries as c
# countries = countries
print(c.countries)
mid_country = len(c.countries) / 2
if (mid_country % 2 == 0):
  print(c.countries[mid_country])
else:
  print(c.countries[int(mid_country)])
  print(c.countries[int(mid_country) + 1 ])

middle_index = len(c.countries) // 2
country1 = c.countries[:middle_index]
country2 = c.countries[middle_index:]

country = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
cn, rus, us, *scandic = country
print(scandic)