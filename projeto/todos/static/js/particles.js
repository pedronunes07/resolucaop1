// Configurações das partículas
const particleConfig = {
    count: 50,
    size: {
        min: 2,
        max: 8
    },
    speed: {
        x: {
            min: -2,
            max: 2
        },
        y: {
            min: 1,
            max: 3
        }
    }
};

// Classe Partícula
class Particle {
    constructor() {
        this.x = Math.random() * window.innerWidth;
        this.y = Math.random() * window.innerHeight;
        this.size = particleConfig.size.min + Math.random() * (particleConfig.size.max - particleConfig.size.min);
        this.speedX = particleConfig.speed.x.min + Math.random() * (particleConfig.speed.x.max - particleConfig.speed.x.min);
        this.speedY = particleConfig.speed.y.min + Math.random() * (particleConfig.speed.y.max - particleConfig.speed.y.min);
    }

    update() {
        this.x += this.speedX;
        this.y += this.speedY;

        // Reset quando sair da tela
        if (this.x > window.innerWidth || this.y > window.innerHeight) {
            this.x = Math.random() * window.innerWidth;
            this.y = -this.size;
        }
    }

    draw(ctx) {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(255, 255, 255, 0.3)';
        ctx.fill();
    }
}

// Gerenciador de partículas
class ParticleSystem {
    constructor() {
        this.canvas = document.createElement('canvas');
        this.ctx = this.canvas.getContext('2d');
        this.particles = [];
        this.init();
    }

    init() {
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
        document.body.appendChild(this.canvas);

        for (let i = 0; i < particleConfig.count; i++) {
            this.particles.push(new Particle());
        }

        this.animate();
    }

    animate() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

        this.particles.forEach(particle => {
            particle.update();
            particle.draw(this.ctx);
        });

        requestAnimationFrame(() => this.animate());
    }

    resize() {
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
    }
}

// Inicialização
let particleSystem;

window.addEventListener('load', () => {
    particleSystem = new ParticleSystem();
});

window.addEventListener('resize', () => {
    if (particleSystem) {
        particleSystem.resize();
    }
});
