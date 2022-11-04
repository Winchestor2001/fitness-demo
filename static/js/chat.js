const chat = document.getElementById('chat')
const chat_exit = document.getElementById('chat_exit')
const chat_submit = document.getElementById('chat_submit')
const chat_body = document.getElementById('chat_body')
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
                 Yana shugullanasizmi
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
    setTimeout(() => {
        const allfirst_btn = document.querySelectorAll('.first_btn')
        // console.log(allfirst_btn);
        allfirst_btn.forEach(allFBtn => {
            allFBtn.addEventListener('click', () => {
                setTimeout(() => {
                    // 2-request
                    let text = `Вы выбрали "${allFBtn.innerHTML}".
                    Какой тип тренировки вы хотите выбрать?`
                    requestFunc(text)
                    createBtnTwo()
                    chat_body.scrollTop = chat_body.scrollHeight
                }, 500)
                setTimeout(() => {
                    const Alltwo_btn = document.querySelectorAll('.two_btn')
                    Alltwo_btn.forEach(AllTBtn => {
                        AllTBtn.addEventListener('click', () => {
                            setTimeout(() => {
                                // 3-request
                                let text = `Вы выбрали тип тренировки "${AllTBtn.innerHTML}".
                                Пожалуйста, укажите пол.`
                                requestFunc(text)
                                createBtnTree()
                                chat_body.scrollTop = chat_body.scrollHeight
                            }, 500)
                            setTimeout(() => {
                                const AllThree_btn = document.querySelectorAll('.three_btn')
                                AllThree_btn.forEach(allThBtn => {
                                    allThBtn.addEventListener('click', () => {
                                        setTimeout(() => {
                                            // 4-request
                                            let text = `Какую область тела вы хотите проработать?`
                                            requestFunc(text)
                                            createBtnFour()
                                            chat_body.scrollTop = chat_body.scrollHeight
                                        }, 500)
                                        setTimeout(() => {
                                            whileFunc()
                                            function whileFunc() {
                                                const AllFour_btn = document.querySelectorAll('.four_btn')
                                                AllFour_btn.forEach(allFoBtn => {
                                                    allFoBtn.addEventListener('click', () => {
                                                        setTimeout(() => {
                                                            // 5-request
                                                            let text = `Вы выбрали группу мышц "${allThBtn.innerHTML}".
                                                            Рассмотрите следующие варианты тренировок:`
                                                            requestFunc(text)
                                                            let text1 = `"8 минут на нижний пресс". Короткое, но эффективное занятие из классических упражнений.`
                                                            let text2 = `"Топ-10 упражнений для похудения живота стоя."
                                                            10 эффективных и разнообразных упражнения стоя.`
                                                            let text3 = `"20 упражнений без прыжков". Эффективная зарядка, которая не только усилит жиросжигание, но и зарядит энергией.`
                                                            let text4 = `"Топ-10 упражнений для похудения в животе".
                                                            10 упражнений для всего пресса и зоны боков.`
                                                            requestFuncLink(text1)
                                                            requestFuncLink(text2)
                                                            requestFuncLink(text3)
                                                            requestFuncLink(text4)
                                                            // createBtnFive()
                                                            chat_body.scrollTop = chat_body.scrollHeight
                                                        }, 500)
                                                    })
                                                })
                                            }
                                        }, 500)
                                    })
                                })
                            }, 500);
                        })
                    })
                }, 500)
            })
        });
    }, 1000)

})
chat_exit.addEventListener('click', () => {
    chat.classList.remove('ative')
})