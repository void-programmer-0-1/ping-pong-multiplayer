
class PingPongGame {
    constructor(canvasId){
        this.canvas = document.getElementById(canvasId);
        this.ctx = this.canvas.getContext("2d");

        // Game Parameters
        this.paddleHeight = 100;
        this.paddleWidth = 15;
        this.ballSize = 10;
        this.ballSpeedX = 5;
        this.ballSpeedY = 3;
        this.playerSpeed = 20;
        this.npcSpeed = 5;

        // player and ball positions
        this.playerX = this.paddleWidth;
        this.playerY = this.canvas.height / 2 - this.paddleHeight / 2;
        this.npcX = this.canvas.width - this.paddleWidth * 2;
        this.npcY = this.canvas.height / 2 - this.paddleHeight / 2;
        this.ballX = this.canvas.width / 2;
        this.ballY = this.canvas.height / 2;

        // scores
        this.playerScore = 0;
        this.npcScore = 0;

        // movement handler
        document.addEventListener("keydown", this.playerHandler.bind(this));
        
        // game loop
        this.gameLoop();
    }

    playerHandler(e){
        e.preventDefault();

        if (e.key === "ArrowUp" && this.playerY > 0) {
            this.playerY -= this.playerSpeed; // Move up
        }
        
        if (e.key === "ArrowDown" && this.playerY < this.canvas.height - this.paddleHeight) {
            this.playerY += this.playerSpeed; // Move down
        }
    }    

    // Reset ball to center
    resetBall() {
        this.ballX = this.canvas.width / 2;
        this.ballY = this.canvas.height / 2;
        this.ballSpeedX = -this.ballSpeedX; // Change direction
    }

    gameLoop(){
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        
        this.ctx.fillStyle = "#fff";
        this.ctx.fillRect(this.playerX, this.playerY, this.paddleWidth, this.paddleHeight);
        this.ctx.fillRect(this.npcX, this.npcY, this.paddleWidth, this.paddleHeight);

        this.ctx.fillRect(this.ballX, this.ballY, this.ballSize, this.ballSize);

        this.ballX += this.ballSpeedX;
        this.ballY += this.ballSpeedY;
        
        // Ball collision with top and bottom
        if (this.ballY <= 0 || this.ballY >= this.canvas.height - this.ballSize) {
            this.ballSpeedY = -this.ballSpeedY;
        }

        // collision detection with player
        if (this.ballX <= this.paddleWidth && this.ballY >= this.playerY && this.ballY <= this.playerY + this.paddleHeight) {
            this.ballSpeedX = -this.ballSpeedX;
        }

        // collision with npc paddle
        if (this.ballX >= this.canvas.width - this.paddleWidth - this.ballSize && this.ballY >= this.npcY && this.ballY <= this.npcY + this.paddleHeight) {
            this.ballSpeedX = -this.ballSpeedX;
        }

        // Check if the ball goes out of bounds
        if (this.ballX <= 0) {
            this.npcScore++;
            this.resetBall();
        } else if (this.ballX >= this.canvas.width - this.ballSize) {
            this.playerScore++;
            this.resetBall();
        }

         // Draw scores
        this.ctx.font = "20px Arial";
        this.ctx.fillText(`Player: ${this.playerScore}`, 20, 30);
        this.ctx.fillText(`Computer: ${this.npcScore}`, this.canvas.width - 160, 30);

        // Request the next frame
        requestAnimationFrame(this.gameLoop.bind(this));
    }
}
