// Get references to modal elements
const modal = document.getElementById('myModal');
const modalContent = document.querySelector('#myModal > div');

// Get references to open and close modal buttons
const openModalButton = document.getElementById('openModalButton');
const closeModalButton = document.getElementById('closeModalButton');
const bar1 = document.getElementById('bar-1');
const bar2 = document.getElementById('bar-2');
const bar3 = document.getElementById('bar-3');

// Variable to track the modal state
let isModalOpen = false;

// Function to toggle the modal
function toggleModal() {
  if (isModalOpen) {
    hideModal();
    bar1.style.transform = 'translate(0, 0px) rotate(0deg)';
    bar2.style.opacity = '1';
    bar3.style.transform = 'translate(0, 0px) rotate(0deg)';
  } else {
    showModal();
    bar1.style.transform = 'translate(0, 8px) rotate(-45deg)';
    bar2.style.opacity = '0';
    bar3.style.transform = 'translate(0, -8px) rotate(45deg)';
  }
}

// Function to show the modal with animation
function showModal() {
  modal.classList.remove('hidden');
  modal.classList.add('pointer-events-auto'); // Enable pointer events
  setTimeout(() => {
    modalContent.classList.remove('scale-0');
  }, 50); // Adding a small delay before applying the animation
  document.body.style.overflow = 'hidden'; // Disable scrolling when the modal is open

  // Change the menu icon to an X

  isModalOpen = true;
}

// Function to hide the modal
function hideModal() {
  modalContent.classList.add('scale-0');
  document.body.style.overflow = ''; // Enable scrolling when the modal is closed

  // Delay hiding the modal container to allow the animation to finish
  setTimeout(() => {
    modal.classList.add('hidden');
    modal.classList.remove('pointer-events-auto'); // Disable pointer events
  }, 300);

  // Change the X back to the menu icon

  isModalOpen = false;
}

// Event listener for the toggle modal button
openModalButton.addEventListener('click', toggleModal);

let valueDisplays = document.querySelectorAll('.num')
let interval = 1500;

valueDisplays.forEach(valueDisplays => {
  let startValue = 0;
  let endValue = parseInt(valueDisplays.getAttribute("data-val"));
  console.log(endValue)
  let duration = Math.floor(interval / endValue);
  let counter = setInterval(function () {
    startValue += 1;
    valueDisplays.textContent = startValue + "+";
    if(startValue == endValue){
      clearInterval(counter);
    }
  }, duration)
})

const pargraphAnim = document.querySelectorAll('.pargraphAnim')
document.addEventListener("scroll", function () {
  pargraphAnim.forEach((pargraphAnim) => {
    pargraphAnim.classList.add("opacity-100")
    pargraphAnim.classList.remove("opacity-0")
    pargraphAnim.classList.add("translate-y-6")
    pargraphAnim.classList.remove("translate-y-0")
  }) 
})
function isInView(element){
  const rect = element.getBoundingClientRect();
  return (
    rect.bottom > 0 && rect.top < (window.innerHeight - 150 || document.documentElement.clientHeight - 150)
  )
}

const swiper = new Swiper('.swiper', {
  loop: true,

  // Set additional parameters for the creative effect
  autoplay: {
    delay: 10000, // Delay between transitions in milliseconds
    disableOnInteraction: true, // Continue autoplay even when user interacts with the slider
  },
  centeredSlides: true,
  centeredSlidesBounds: true,
//   pagination: {
//     el: '.swiper-pagination',
//   },

  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
});

