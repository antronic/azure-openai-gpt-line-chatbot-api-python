# Stage 1: Build container
FROM --platform=linux/amd64 python:3.11.2-alpine as builder

WORKDIR /app

# Copy the Poetry files
COPY pyproject.toml poetry.lock ./

# Install Poetry
RUN pip install poetry

# Install project dependencies
RUN poetry install --no-root

# Export the dependencies to a requirements.txt file
RUN poetry export -f requirements.txt -o requirements.txt

# Copy the application code
COPY . .

# Stage 2: Final image
FROM python:3.11.2-alpine

WORKDIR /app

# Copy the built artifacts from the builder stage
COPY --from=builder /app/ ./

# Install the application from requirements.txt
RUN pip install -r requirements.txt

# Set the entry point
CMD ["python", "main.py"]