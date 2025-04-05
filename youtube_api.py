from googleapiclient.discovery import build

api_key = 'XYZ'


video_id = 's86-Z-CbaHA' 


request = youtube.videos().list(
    part="statistics", 
    id=video_id
)


response = request.execute()

print("Full response:", response)


if 'items' in response and len(response['items']) > 0:
    video_data = response['items'][0]
    views = video_data['statistics']['viewCount']
    likes = video_data['statistics']['likeCount']

    dislikes = video_data['statistics'].get('dislikeCount', 'Not available')
    comments = video_data['statistics']['commentCount']

    print(f"Video ID: {video_id}")
    print(f"Views: {views}")
    print(f"Likes: {likes}")
    print(f"Dislikes: {dislikes}")
    print(f"Comments: {comments}")
else:
    print(f"No data found for video ID: {video_id}")
