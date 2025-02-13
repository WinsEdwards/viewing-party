# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movies_dict = {}
    if not title or not genre or not rating:
        return None
    else:
        movies_dict["title"] = title
        movies_dict["genre"] = genre
        movies_dict["rating"] = rating 
    return movies_dict

def add_to_watched(user_data, movie):
    watched_list = user_data["watched"]
    is_valid = True

    ### checking that watched_list is not empty
    if watched_list:
    ### checking that title is not already in watched_list keys
        for movie_dict in watched_list:
            if movie_dict["title"] == movie["title"]:
                is_valid = False
    
    ### if movie is not duplicate, append to watched_list
    if is_valid:
        watched_list.append(movie)

    return user_data

def add_to_watchlist(user_data, movie):  
    want_to_watch_list = user_data["watchlist"]
    is_valid = True

    ### checking that want_to_watch_list is not empty
    if want_to_watch_list:
    ### checking that title is not already in want_to_watch_list keys
        for movie_dict in want_to_watch_list:
            if movie_dict["title"] == movie["title"]:
                is_valid = False
    
    ### if movie is not duplicate, append to want_to_watch_list
    if is_valid:
        want_to_watch_list.append(movie)

    return user_data

def watch_movie(user_data, title):
    want_to_watch_list = user_data["watchlist"]
    watched_list = user_data["watched"]
    ##iterating through want_to_watch_list to see if title is present
    for movie_dict in want_to_watch_list:
        ##if title present, remove from want_to_watch list and add to watched_list
        if movie_dict["title"] == title:
            watched_list.append(movie_dict)
            want_to_watch_list.remove(movie_dict)

    return user_data



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------



def get_watched_avg_rating(user_data):
    watched_list = user_data["watched"]
    avg_rating = 0.0
    ##empty watch list is 0.0 avg rating
    if len(watched_list) == 0:
        return avg_rating
    else:
        ##iterate through watched_list, add all ratings and then divide by length of watched_list
        for movie_dict in watched_list:
            avg_rating += movie_dict["rating"]
        avg_rating = avg_rating/len(watched_list)
    return avg_rating


def get_most_watched_genre(user_data):
    watched_list = user_data["watched"]
    genre_dict = {}
    ##return None for empty list
    if len(watched_list) == 0:
        return None
    else:
        #iterate through watched_list for genre and add genre to genre_dict. 
        # Increment value according to genre count.
        for movie_dict in watched_list:
            if movie_dict["genre"] not in genre_dict.keys():
                genre_dict[movie_dict["genre"]] = 1
            else:
                genre_dict[movie_dict["genre"]] += 1
    ##return key that has the max value in genre_dict            
    return max(genre_dict, key=genre_dict.get)

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    watched_list = user_data["watched"]
    friends_watched_list = user_data["friends"]
    watched_list_set = set()
    friends_watched_list_set = set()
    unique_watched_list = []

### if watched_list empty, return empty list
    if not watched_list:
        return []
### if friends_watched_list empty, return user's watched_list
    elif not friends_watched_list:
        return watched_list
### creating set of user's watched titles
    for movie_dict in watched_list:
        watched_list_set.add(movie_dict["title"])
### creating set of user's friends' watched titles
    for friend in friends_watched_list:
        for movie_dict in friend["watched"]:
            friends_watched_list_set.add(movie_dict["title"])
### checking for titles in user watched_list that are not also present in friends_watched_list
    unique_watched_set = watched_list_set - friends_watched_list_set
### if complete overlap, return empty list
    if len(unique_watched_set) == 0:
        return []
### else return list of dictionaries with title, genre, rating for unique items
    for title in unique_watched_set:
        for movie_dict in watched_list:
            if movie_dict["title"] == title:
                unique_watched_list.append(movie_dict)
    
    return unique_watched_list

def get_friends_unique_watched(user_data):
    watched_list = user_data["watched"]
    friends_watched_list = user_data["friends"]
    watched_list_set = set()
    friends_watched_list_set = set()
    friends_unique_watched_list = []

### if watched_list empty, return empty list
    if not friends_watched_list:
        return []
### creating set of user's watched titles [same as prior]
    for movie_dict in watched_list:
        watched_list_set.add(movie_dict["title"])
### creating set of user's friends' watched titles [same as prior]
    for friend in friends_watched_list:
        for movie_dict in friend["watched"]:
            friends_watched_list_set.add(movie_dict["title"])
### checking for titles in user watched_list that are not also present in friends_watched_list
    friends_unique_watched_set = friends_watched_list_set - watched_list_set
### if complete overlap, return empty list
    if len(friends_unique_watched_set) == 0:
        return []
### else return list of dictionaries with title, genre, rating for unique items
    for title in friends_unique_watched_set:
        for friend in friends_watched_list:
            for movie_dict in friend["watched"]:
                if movie_dict["title"] == title:
                    # for entry in friends_unique_watched_list:
                        if movie_dict not in friends_unique_watched_list:
                            friends_unique_watched_list.append(movie_dict)
                    
    return friends_unique_watched_list


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    friends_unique_watched_list = get_friends_unique_watched(user_data)
    subscriptions_list = user_data["subscriptions"]
    recommended_movies = []

    ### iterating through movie dictionaries in friends_unique_watched_list to find movies user has 
    ### access to via subscription
    for movie_dict in friends_unique_watched_list:
        # for movie_dict in friend["watched"]:
            ### determining if a given movie that user has not seen is available via subscription service, 
            ### if so append to recommend_movies
        if movie_dict["host"] in subscriptions_list:
            recommended_movies.append(movie_dict)

    return recommended_movies


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


def get_new_rec_by_genre(user_data):
    friends_unique_watched_list = get_friends_unique_watched(user_data)
    recommended_movies = []
    most_watched_genre = get_most_watched_genre(user_data)
    print(most_watched_genre)
    for movie_dict in friends_unique_watched_list:
        ### determining if a given movie that user has not seen is of preferred genre, 
        ### if so append to recommend_movies
        if movie_dict["genre"] == most_watched_genre:
            recommended_movies.append(movie_dict)

    return recommended_movies


def get_rec_from_favorites(user_data):
    user_unique_movies = get_unique_watched(user_data)
    recommended_movies = []
    favorites_list = user_data["favorites"]
    for movie_dict in user_unique_movies:
        ### determining if a given movie that user's friend has not seen is in favorites list, 
        ### if so append to recommend_movies
        if movie_dict in favorites_list:
            recommended_movies.append(movie_dict)

    return recommended_movies

