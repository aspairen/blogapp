# Importing necessary modules and functions
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm


# Function to retrieve and display all blogs
def retrieve_blogs(request):
    # Query all blog objects from the database
    blogs = Blog.objects.all()
    # Render the 'retrieve_blogs.html' template with the blogs data
    return render(request, 'blog/retrieve_blogs.html', {'blogs': blogs})

# Function to create a new blog
def create_blog(request):
    if request.method == 'POST':
        # Create a form instance with POST data
        form = BlogForm(request.POST)
        if form.is_valid():
            # Save the form data to create a new blog
            form.save()
            # Redirect to the retrieve_blogs view after saving
            return redirect('retrieve_blogs')
    else:
        # If the request is GET, create a new empty form instance
        form = BlogForm()
    # Render the 'create_blog.html' template with the form
    return render(request, 'blog/create_blog.html', {'form': form})

# Function to update an existing blog
def update_blog(request, pk):
    # Retrieve the blog object with the given primary key (pk) or return 404 if not found
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        # Create a form instance with POST data and the existing blog instance
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            # Save the form data to update the blog
            form.save()
            # Redirect to the retrieve_blogs view after saving
            return redirect('retrieve_blogs')
    else:
        # If the request is GET, create a form instance with the existing blog instance
        form = BlogForm(instance=blog)
    # Render the 'update_blog.html' template with the form
    return render(request, 'blog/update_blog.html', {'form': form})


    