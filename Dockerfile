# Use the official lightweight Python image
FROM python:3.10-slim

# Prevent Python from writing .pyc files to disk and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

# Create a non-root user for security
RUN adduser --disabled-password --gecos "" serviceuser

# Set the working directory
WORKDIR /app

# Copy the pyproject.toml first to leverage Docker layer caching
COPY pyproject.toml ./

# Install the package and its production dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir .

# Copy the application source code and the ML artifacts
COPY src/ ./src/
COPY artifacts/ ./artifacts/

# Transfer ownership to the non-root user and switch contexts
RUN chown -R serviceuser:serviceuser /app
USER serviceuser

# Expose the application port
EXPOSE 8000

# Boot the FastAPI application via Uvicorn
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]