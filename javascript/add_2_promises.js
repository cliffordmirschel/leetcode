var addTwoPromises = async function(promise1, promise2) {
    num1 = await(promise1)
    num2 = await(promise2)
    const new_promise = new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(num1 + num2);
        }, 300);
});

    return new_promise
};