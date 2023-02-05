from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    platform = request.user_agent.to_header()
    print(platform)
    return render_template( 'painel.html' , platform=platform)

if __name__ == '__main__':
    app.run( debug=True , host='0.0.0.0' )
