import deviantart

da = deviantart.Api(29316, "4ed6af8f905b519e6e05f82247ee7dee")

response = da.browse(endpoint='tags', tag='animalphotography', offset=58, limit=24)
print(response['results'])
print(response['has_more'])
print(response['next_offset'])
for deviation in response['results']:
    print('-----')
    print(deviation.title)
    print("Maturity", deviation.is_mature)
    print(deviation.author.username)
    print(deviation.url)
    print('-----')



