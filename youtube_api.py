from googleapiclient.discovery import build

# Your API key (ensure this is correct)
api_key = 'AIzaSyAouzKmqcH5U9FkWptBX7qCuTP-sIG9Nc0'

# Correct video ID (exclude any part after & symbol)
video_id = 's86-Z-CbaHA'  # Corrected video ID

# Initialize the YouTube API client
youtube = build('youtube', 'v3', developerKey=api_key)

# Request to fetch only the statistics (no snippet)
request = youtube.videos().list(
    part="statistics",  # Only fetch statistics (views, likes, dislikes, etc.)
    id=video_id
)

# Execute the request and capture the response
response = request.execute()

# Debug: print the entire response to see what the API returns
print("Full response:", response)

# Check if response contains the 'items' key and print the relevant data
if 'items' in response and len(response['items']) > 0:
    video_data = response['items'][0]
    views = video_data['statistics']['viewCount']
    likes = video_data['statistics']['likeCount']
    # Dislike count is not available anymore, handle gracefully
    dislikes = video_data['statistics'].get('dislikeCount', 'Not available')
    comments = video_data['statistics']['commentCount']
    
    # Print the results
    print(f"Video ID: {video_id}")
    print(f"Views: {views}")
    print(f"Likes: {likes}")
    print(f"Dislikes: {dislikes}")
    print(f"Comments: {comments}")
else:
    print(f"No data found for video ID: {video_id}")