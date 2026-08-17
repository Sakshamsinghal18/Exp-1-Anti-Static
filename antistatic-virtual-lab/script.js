document.addEventListener('DOMContentLoaded', () => {
    let currentStep = 1;
    const totalSteps = 30;

    const stepImage = document.getElementById('step-image');
    const currentStepText = document.getElementById('current-step');
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');

    function updateView() {
        currentStepText.textContent = currentStep;
        prevBtn.disabled = currentStep === 1;
        nextBtn.disabled = currentStep === totalSteps;
        stepImage.src = `step${currentStep}.png`;
    }

    prevBtn.addEventListener('click', () => {
        if (currentStep > 1) { currentStep--; updateView(); }
    });

    nextBtn.addEventListener('click', () => {
        if (currentStep < totalSteps) { currentStep++; updateView(); }
    });

    updateView();
});
