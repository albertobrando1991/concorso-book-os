/* Capitale Personale — slide controller + inline editor */
class SlidePresentation {
    constructor() {
        this.slides = document.querySelectorAll(".slide");
        this.currentSlide = 0;
        this.stage = document.getElementById("deckStage");
        this.progress = document.getElementById("progressFill");
        this.pageCount = document.getElementById("pageCount");
        this.wheelLock = false;
        this.setupStageScale();
        this.setupKeyboardNav();
        this.setupTouchNav();
        this.setupWheelNav();
        this.showSlide(0);
    }

    setupStageScale() {
        const scale = () => {
            const factor = Math.min(window.innerWidth / 1920, window.innerHeight / 1080);
            const x = (window.innerWidth - 1920 * factor) / 2;
            const y = (window.innerHeight - 1080 * factor) / 2;
            this.stage.style.transform = `translate(${x}px, ${y}px) scale(${factor})`;
        };
        scale();
        window.addEventListener("resize", scale);
    }

    setupKeyboardNav() {
        document.addEventListener("keydown", (e) => {
            if (e.target.getAttribute("contenteditable")) return;
            if (["ArrowRight", "ArrowDown", "PageDown", " "].includes(e.key)) {
                e.preventDefault();
                this.next();
            } else if (["ArrowLeft", "ArrowUp", "PageUp"].includes(e.key)) {
                e.preventDefault();
                this.prev();
            } else if (e.key === "Home") {
                e.preventDefault();
                this.showSlide(0);
            } else if (e.key === "End") {
                e.preventDefault();
                this.showSlide(this.slides.length - 1);
            }
        });
    }

    setupTouchNav() {
        let startX = 0;
        document.addEventListener("touchstart", (e) => {
            startX = e.changedTouches[0].screenX;
        }, { passive: true });
        document.addEventListener("touchend", (e) => {
            const dx = e.changedTouches[0].screenX - startX;
            if (Math.abs(dx) < 50) return;
            if (dx < 0) this.next();
            else this.prev();
        }, { passive: true });
    }

    setupWheelNav() {
        window.addEventListener("wheel", (e) => {
            if (this.wheelLock) return;
            if (Math.abs(e.deltaY) < 20) return;
            this.wheelLock = true;
            if (e.deltaY > 0) this.next();
            else this.prev();
            setTimeout(() => { this.wheelLock = false; }, 500);
        }, { passive: true });
    }

    next() { this.showSlide(this.currentSlide + 1); }
    prev() { this.showSlide(this.currentSlide - 1); }

    showSlide(index) {
        this.currentSlide = Math.max(0, Math.min(index, this.slides.length - 1));
        this.slides.forEach((slide, i) => {
            slide.classList.toggle("active", i === this.currentSlide);
            slide.classList.toggle("visible", i === this.currentSlide);
        });
        const total = this.slides.length;
        const n = this.currentSlide + 1;
        if (this.progress) this.progress.style.width = `${(n / total) * 100}%`;
        if (this.pageCount) {
            this.pageCount.textContent = String(n).padStart(2, "0") + " / " + String(total).padStart(2, "0");
        }
    }
}

class InlineEditor {
    constructor() {
        this.isActive = false;
        this.key = document.body.dataset.editKey || "cp-slide-edits";
        this.toggleBtn = document.getElementById("editToggle");
        this.restore();
    }
    toggleEditMode() {
        this.isActive = !this.isActive;
        document.body.classList.toggle("editing", this.isActive);
        if (this.toggleBtn) this.toggleBtn.classList.toggle("active", this.isActive);
        document.querySelectorAll("h1,h2,h3,p,span,strong,td").forEach((el) => {
            el.setAttribute("contenteditable", this.isActive ? "true" : "false");
        });
        if (!this.isActive) this.save();
    }
    save() {
        const stage = document.getElementById("deckStage");
        if (stage) localStorage.setItem(this.key, stage.innerHTML);
    }
    restore() {
        const saved = localStorage.getItem(this.key);
        const stage = document.getElementById("deckStage");
        if (saved && stage) stage.innerHTML = saved;
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const deck = new SlidePresentation();
    const editor = new InlineEditor();
    const hotzone = document.querySelector(".edit-hotzone");
    const editToggle = document.getElementById("editToggle");
    let hideTimeout = null;
    const showToggle = () => {
        clearTimeout(hideTimeout);
        if (editToggle) editToggle.classList.add("show");
    };
    const hideToggle = () => {
        hideTimeout = setTimeout(() => {
            if (!editor.isActive && editToggle) editToggle.classList.remove("show");
        }, 400);
    };
    if (hotzone && editToggle) {
        hotzone.addEventListener("mouseenter", showToggle);
        hotzone.addEventListener("mouseleave", hideToggle);
        editToggle.addEventListener("mouseenter", showToggle);
        editToggle.addEventListener("mouseleave", hideToggle);
        hotzone.addEventListener("click", () => editor.toggleEditMode());
        editToggle.addEventListener("click", () => editor.toggleEditMode());
    }
    document.addEventListener("keydown", (e) => {
        if ((e.key === "e" || e.key === "E") && !e.target.getAttribute("contenteditable")) {
            editor.toggleEditMode();
        }
    });
    window.addEventListener("beforeunload", () => { if (editor.isActive) editor.save(); });
    window.cpDeck = deck;
});
