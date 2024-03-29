let currentQuestion = 0;
const questions = document.querySelectorAll('.question');

function showQuestion(index) {
    questions.forEach((question, idx) => {
        if (idx === index) {
            question.classList.add('active');
        } else {
            question.classList.remove('active');
        }
    });
}

function nextQuestion() {
    if (currentQuestion < questions.length - 1) {
        currentQuestion++;
        showQuestion(currentQuestion);
    }
}

function prevQuestion() {
    if (currentQuestion > 0) {
        currentQuestion--;
        showQuestion(currentQuestion);
    }
}

function skipQuestion() {
    nextQuestion();
}

showQuestion(currentQuestion);
