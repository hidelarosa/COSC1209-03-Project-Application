from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Render the HTML page
    return render_template('index.html')

@app.route('/api/threads/<int:thread_id>/full', methods=['GET'])
def get_thread_data(thread_id):
    try:
        # Use ECS service names as hostnames for internal communication
    thread_response = requests.get(f'http://threads-service.fargate-microservices:3002/api/threads/{thread_id}')
    posts_response = requests.get(f'http://posts-service.fargate-microservices:3001/api/posts/in-thread/{thread_id}')
    users_response = requests.get(f'http://users-service.fargate-microservices:3003/api/users')


        # Check if responses are successful
        if thread_response.status_code == 200 and posts_response.status_code == 200 and users_response.status_code == 200:
            thread_data = thread_response.json()
            posts_data = posts_response.json()
            users_data = users_response.json()

            return jsonify({
                'thread': thread_data,
                'posts': posts_data,
                'users': users_data
            })
        else:
            return jsonify({'error': 'Failed to fetch data from microservices'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Ensure the app listens on all interfaces
    app.run(host='0.0.0.0', port=5000)
