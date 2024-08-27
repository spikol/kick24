(function () {

	/**
	 * Prevent navigation on <a href="#">
	 */

	document.querySelectorAll('a[href="#"]').forEach((el) => {
		el.addEventListener('click', (ev) => {
			ev.preventDefault();
		});
	});

})();

$(document).ready(function () {


});

(function () {

	const toggler = document.querySelector('.section-navbar a.-menu-toggler');
	const target = document.querySelector('.section-navbar .-login-signup');
	const backBtn = document.querySelector('.icon-area');

	if (toggler) {
		toggler.addEventListener('click', function (el) {
			target.classList.toggle('-show');
		});
		if (backBtn) {
			toggler.addEventListener('click', function (el) {
				backBtn.classList.toggle('top-pos');
				console.log(backBtn);
			});
		}
	}
})();

(function () {

	const qrTypes = document.querySelectorAll('.section-qr-types .-qr-type');
	qrTypes.forEach((qrType) => {
		qrType.addEventListener('click', function () {
			document.querySelector('.section-qr-types .-qr-type.-active').classList.remove('-active');
			this.classList.add('-active');
			// const qrTypeInfo = document.querySelector('.section-qr-types .-qr-type-info.-show');
			// const target = document.querySelector(this.getAttribute('data-target'));
			const target = document.querySelector('.-qr-type-info.-show');
			target.classList.add('-fading');

			// document.getElementById('showCasePreview').contentWindow.postMessage({
			// 	live:true,
			// 	step:2,
			// 	static:true,
			// 	type:this.getAttribute('data-target')
			// },'<?=LANDING_PAGE_URL?>'); 

			setTimeout(() => {
				target.classList.remove('-fading')
				// target.classList.remove('-show', '-fading');
				// target.classList.add('-fading', '-show');
				// requestAnimationFrame(() => {
				// 	target.classList.remove('-fading');
				// });
			}, 400);
		});
	});

})();

(function () {

	if (!document.querySelector('.section-design-faq')) {
		return;
	}

	const container = document.querySelector('.section-design-faq .-question-tab-list');
	const leftArrow = document.querySelector('.section-design-faq .-arrow.-left');
	const rightArrow = document.querySelector('.section-design-faq .-arrow.-right');
	const langType = document.documentElement.lang;
	console.log(langType);

	leftArrow.addEventListener('click', function () {
		console.log("click");
		container.scroll({ left: 0, behavior: 'smooth' });
	});

	if(langType == "ar"){
		rightArrow.addEventListener('click', function () {
			container.scroll({ left: container.scrollLeft - 403, behavior: 'smooth' });
		});
	}else{
		rightArrow.addEventListener('click', function () {
			container.scroll({ left: container.scrollLeft + 403, behavior: 'smooth' });
		});
	}

	const questionTabs = document.querySelectorAll('.section-design-faq .-question-tab');
	questionTabs.forEach((questionTab) => {
		questionTab.addEventListener('click', function () {
			document.querySelector('.section-design-faq .-question-tab.-active').classList.remove('-active');
			this.classList.add('-active');
			const questionAnswer = document.querySelector('.section-design-faq .-question-answer.-show');
			const target = document.querySelector(this.getAttribute('data-target'));
			questionAnswer.classList.add('-fading');
			setTimeout(() => {
				questionAnswer.classList.remove('-show', '-fading');
				target.classList.add('-fading', '-show');
				requestAnimationFrame(() => {
					target.classList.remove('-fading');
				});
			}, 200);
		});
	});

})();

(function () {

	const answers = document.querySelectorAll('.section-concepts .-answer');

	window.addEventListener('load', () => {
		answers.forEach((answer) => {
			if (answer.scrollHeight !== answer.clientHeight) {
				answer.classList.add('-overflowing');
			}
		});
	});

	const conceptModal = document.querySelector('.concept-modal');
	const readMores = document.querySelectorAll('.section-concepts .-read-more');

	readMores.forEach((readMore) => {
		readMore.addEventListener('click', function () {

			document.body.classList.add('modal-open');
			conceptModal.classList.add('-show', '-fading');
			requestAnimationFrame(() => {
				requestAnimationFrame(() => {
					conceptModal.classList.remove('-fading');
				});
			})

			const container = readMore.closest('.-question-answer');
			const iconEl = container.querySelector('.-icon-wrapper-circle');
			const questionEl = container.querySelector('.-question');
			const answerEl = container.querySelector('.-answer');

			conceptModal.querySelector('.-icon-wrapper-circle').innerHTML = iconEl.innerHTML;
			conceptModal.querySelector('.-question').innerHTML = questionEl.outerHTML;
			conceptModal.querySelector('.-answer').innerHTML = answerEl.outerHTML;
		});
	});

	const modals = document.querySelectorAll('.modal:not(.help-modal):not(.new-dl-modal)');

	modals.forEach((modal) => {
		const close = modal.querySelector('.-close');
		close?.addEventListener('click', function () {
			closeModal();
		});

		const box = modal.querySelector('.-modal-box');

		modal.addEventListener('click', function (ev) {
			if (!(box?.contains(ev.target) || box === ev.target)) {
				closeModal();
			}
		});

		function closeModal() {
			modal.classList.add('-fading');
			document.body.classList.remove('modal-open');
			setTimeout(() => {
				modal.classList.remove('-show', '-fading');
			}, 400);
		}
	});



})();

(function () {

	const togglers = document.querySelectorAll('.accordion .-accordion-toggler');

	for (let i = 0; i < togglers.length; i++) {

		const toggle = function (el) {

			const panel = el.nextElementSibling;

			if (!panel.classList.contains('-accordion-panel')) {
				return;
			}

			if (panel.style.maxHeight) {
				panel.style.maxHeight = null;
			} else {
				panel.style.maxHeight = panel.scrollHeight + 'px';
			}
			el.classList.toggle('-active');
		};

		togglers[i].addEventListener('click', function () {
			toggle(this);
		});

		togglers[i].addEventListener('keydown', function (ev) {
			if (ev.key === ' ') {
				ev.preventDefault();
				toggle(this);
			}
		});
	}

})();

(function () {
	const revealPasswordButtons = document.querySelectorAll('button.-reveal-password');
	revealPasswordButtons.forEach((revealPasswordButton) => {
		revealPasswordButton.addEventListener('click', function () {			
			const input = document.querySelector(revealPasswordButton.getAttribute('data-target'));
			const eyeOn = document.querySelector('#eyeOn');
			const eyeOff = document.querySelector('#eyeOff');
			if (input.type === 'password') {
				input.type = 'text';
				eyeOn.classList.remove('d-none');
				eyeOff.classList.add('d-none');
			} else {
				eyeOff.classList.remove('d-none');
				eyeOn.classList.add('d-none');
				input.type = 'password';
			}
		});
	});

})();


$('.plan-section .package').each((_, package) => {
	const addToCart = $(package).find('a.add-to-cart');
	$(package).find('button.plan-btn, button.annual-time-btn').on('click', function () {
		addToCart[0].click();
	});
});

// Home Footer Language Dropdown Menu

const languageDropdown = document.getElementsByClassName('footer-lang-dropdown-menu')[0];
const lang_drop_down_btn = document.getElementById('lang-drop-down');

try{
	lang_drop_down_btn.onclick = () =>{
		languageDropdown.removeAttribute('hidden');
	}
}catch(e){}

document.addEventListener('click', function (event) {
    if (lang_drop_down_btn != null && lang_drop_down_btn != undefined && !event.target.matches('#' + lang_drop_down_btn.id)) {
        languageDropdown?.setAttribute('hidden',true);
    }
});

