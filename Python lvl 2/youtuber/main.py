
import googleapiclient.discovery

KEY = 'API_KEY'

CHANNEL_NAME = 'TheMimuro'
CHANNEL_ID = 'UCwRsKnOhmWB5jus__D56c7Q'

youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=KEY)


def get_video_from_channel(channel_name):
    playlist_id = get_playlist_id(channel_name)

    request = youtube.playlistItems().list(
        part="snippet,contentDetails",
        maxResults=10,
        playlistId="PLKPCBJzaFa67VRnzFLSF3ZVnnA5x3zCpP"

    )

    response = request.execute()


    ids = []
    for video in response['items']:

        ids.append(video['snippet']['resourceId']['videoId'])
    return ids


def get_playlist_id(channel_name):
    response = youtube.channels().list(
        part="contentDetails",
        forUsername=channel_name
    ).execute()


    return response['items'][0]['contentDetails']['relatedPlaylists']['uploads']


def print_videos_info(videos):


    response = youtube.videos().list(
        part='statistics,snippet',
        id=','.join(videos)
    ).execute()

    for video in response['items']:

        print('Название: ', video['snippet']['title'])
        print('Просмотры: ', video['statistics']['viewCount'])
        print('Лайки: ', video['statistics']['likeCount'])
        #print('Комментарии: ', video['statistics']['commentCount'])

        print('====')

if __name__ == '__main__':

    videos = get_video_from_channel(CHANNEL_NAME)
    print_videos_info(videos)
