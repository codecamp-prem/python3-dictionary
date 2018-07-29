Beatles_Discography = {'The Game': 1980, 'A Night at the Opera': 1975, 'Jazz': 1978, 'Queen II': 1974, 'A Day at the Races': 1976, 'News of the World': 1977, 'Queen': 1973, 'Sheer Heart Attack': 1974}
def most_prolific(Beatles_Discography):
    year = {}
    for album_title in Beatles_Discography:
        if Beatles_Discography[album_title] in year:
            year[Beatles_Discography[album_title]] += 1
        else:
            year[Beatles_Discography[album_title]] = 1
    high_release = []
    total_album_realse_in_yr = 0;
    for yr in year:
        high_release.append(year[yr])
    high_release_set = set(high_release)
    max_in_set = max(high_release_set)

    high_release = []
    for yr in year:
        if year[yr] == max_in_set:
            high_release.append(yr)
    if len(high_release) > 1:
        print(high_release)
    else:
        print(high_release[0])

most_prolific(Beatles_Discography)
