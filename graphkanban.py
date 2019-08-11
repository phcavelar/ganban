from core import app, db
from core.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {
      "db":db,
      "User": User,
      "Post": Post,
    }
#end make_shell_context
