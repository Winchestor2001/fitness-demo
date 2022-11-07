const chat = document.getElementById('chat')
const chat_exit = document.getElementById('chat_exit')
const chat_submit = document.getElementById('chat_submit')
const chat_body = document.getElementById('chat_body')
let user_selected = []
function requestFunc(text) {
    const messageRequest = document.createElement('div')
    messageRequest.innerHTML = `
    <div class="request">
        <div class="message">
            ${text}
        </div>
     </div>
    `
    chat_body.appendChild(messageRequest)
}
function requestFuncLink(text, link) {
    const messageRequest = document.createElement('div')
    messageRequest.innerHTML = `
    <div class="request">
        <a href='${link}'>
            <div class="message">
                ${text}
            </div>
        </a>
     </div>
    `
    chat_body.appendChild(messageRequest)
}
function createBtnFirst() {
    const messageBtn = document.createElement('div')
    messageBtn.innerHTML = `
        <div class='response'>
            <div class="message first_btn cursor">
                Низкая интенсивность
            </div>
        </div>
        <div class='response'>
            <div class="message first_btn cursor">
                Умеренная интенсивность
            </div>
        </div>
        <div class='response'>
            <div class="message first_btn cursor">
                Средняя интенсивность
            </div>
        </div>
        <div class='response'>
            <div class="message first_btn cursor">
                Большая интенсивность
            </div>
        </div>`
    chat_body.appendChild(messageBtn)
}
function createBtnTwo() {
    const messageBtn = document.createElement('div')
    messageBtn.innerHTML = `
        <div class='response'>
            <div class="message two_btn cursor">
                Для набора мышечной массы
            </div>
        </div>
        <div class='response'>
            <div class="message two_btn cursor">
                Для похудения
            </div>
        </div>`
    chat_body.appendChild(messageBtn)
}
function createBtnTree() {
    const messageBtn = document.createElement('div')
    messageBtn.innerHTML = `
        <div class='response'>
            <div class="message three_btn cursor">
            Женщина
            </div>
        </div>
        <div class='response'>
            <div class="message three_btn cursor">
            Мужчина
            </div>
        </div>`
    chat_body.appendChild(messageBtn)
}
function createBtnFour() {
    const messageBtn = document.createElement('div')
    messageBtn.innerHTML = `
        <div class='response'>
            <div class="message four_btn cursor">
            Руки
            </div>
        </div>
        <div class='response'>
            <div class="message four_btn cursor">
            Грудь
            </div>
        </div>
        <div class='response'>
            <div class="message four_btn cursor">
            Спина
            </div>
        </div>
        <div class='response'>
            <div class="message four_btn cursor">
            Живот
            </div>
        </div>
        <div class='response'>
            <div class="message four_btn cursor">
            Ягодицы
            </div>
        </div>
        <div class='response'>
            <div class="message four_btn cursor">
            Ноги
            </div>
        </div>
        `
    chat_body.appendChild(messageBtn)
}
function createBtnFive() {
    const messageBtn = document.createElement('div')
    messageBtn.innerHTML = `
        <div class='response'>
            <div class="message five_btn cursor">
            Спасибо! Хочу попробовать ещё!
            </div>
        </div>`
    chat_body.appendChild(messageBtn)
}
chat_submit.addEventListener('click', () => {
    chat.classList.add('ative')
    setTimeout(() => {
        // 1-request
        chat_body.innerHTML = `
        <div class="request">
            <div class="message">
                Здравствуйте! Какую тренировку вы хотите подобрать?
            </div>
        </div>`
    }, 500)
    setTimeout(() => {
        createBtnFirst()
    }, 1000)

})
chat_body.addEventListener('click', (e) => {
    let thIs = e.target
    // console.log(thIs);
    if (e.target.classList.contains("first_btn")) {
        // 2-request
        let text = `Вы выбрали "${e.target.innerHTML}". Какой тип тренировки вы хотите выбрать?`
        requestFunc(text)
        createBtnTwo()
        chat_body.scrollTop = chat_body.scrollHeight
        user_selected.push(e.target.innerHTML)
    }
    else if (e.target.classList.contains("two_btn")) {
        // 3-request
        let text = `Вы выбрали тип тренировки "${e.target.innerHTML}". Пожалуйста, укажите пол.`
        requestFunc(text)
        createBtnTree()
        chat_body.scrollTop = chat_body.scrollHeight
        user_selected.push(e.target.innerHTML)
    }
    else if (e.target.classList.contains("three_btn")) {
        // 4-request
        let text = `Какую область тела вы хотите проработать?`
        requestFunc(text)
        createBtnFour()
        user_selected.push(e.target.innerHTML)
        chat_body.scrollTop = chat_body.scrollHeight
    }
    else if (e.target.classList.contains("four_btn")) {
        // 5-request
        let text = `Вы выбрали группу мышц "${e.target.innerHTML}".
        Рассмотрите следующие варианты тренировок:`
        user_selected.push(e.target.innerHTML)
        requestFunc(text)
        ajaxRequest(user_selected);
        // let text1 = `"8 минут на нижний пресс". Короткое, но эффективное занятие из классических упражнений.`
        // let text2 = `"Топ-10 упражнений для похудения живота стоя." 10 эффективных и разнообразных упражнения стоя.`
        // let text3 = `"20 упражнений без прыжков". Эффективная зарядка, которая не только усилит жиросжигание, но и зарядит энергией.`
        // let text4 = `"Топ-10 упражнений для похудения в животе". 10 упражнений для всего пресса и зоны боков.`
        // requestFuncLink(text1)
        // requestFuncLink(text2)
        // requestFuncLink(text3)
        // requestFuncLink(text4)
        // createBtnFive()
        chat_body.scrollTop = chat_body.scrollHeight
    }
    else if (e.target.classList.contains("five_btn")) {
        // 4-request
        let text = `Какую тренировку вы хотите подобрать?`
        requestFunc(text)
        createBtnFour()
        chat_body.scrollTop = chat_body.scrollHeight
        user_selected.push(e.target.innerHTML)
    }
})
chat_exit.addEventListener('click', () => {
    chat.classList.remove('ative')
})