#!/bin/zsh

# build.sh
build_docker() {
    echo "🔨 Building Docker images..."
    docker-compose build
}

# run.sh
run_docker() {
    echo "🖥️  Starting interactive session..."
    docker-compose run --rm app
}

# Main menu
echo "ETL Docker Manager"
echo "1. Build Docker images"
echo "2. Run interactive session"
echo "3. Build and run"
echo "4. Stop all containers"
echo "5. Exit"

read "choice?Choose an option (1-5): "

case $choice in
    1) build_docker ;;
    2) run_docker ;;
    3) build_docker && run_docker ;;
    4) docker-compose down ;;
    5) exit 0 ;;
    *) echo "Invalid option" ;;
esac