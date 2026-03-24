FROM python:3.12-slim

# Set working directory inside container
WORKDIR /api-tests

# Copy dependency list
COPY requirements.txt .

# Install Python dependencies
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy everything into container (tests + run.sh)
COPY . .

# Ensure run.sh is executable
RUN chmod +x run.sh

# Default command: execute your test runner
CMD ["./run.sh"]