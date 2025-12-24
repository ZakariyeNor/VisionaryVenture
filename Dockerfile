FROM node:20-alpine

# Install Python, pip, and build dependencies
RUN apk add --no-cache python3 py3-pip make g++ gcc

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./
RUN npm install

# Copy requirements and install Python dependencies with --break-system-packages
COPY requirements.txt .
RUN pip3 install --break-system-packages -r requirements.txt

# Copy application files
COPY . .

# Expose port (adjust if needed)
EXPOSE 8080

# Run the application
CMD ["node", "index.js"]
