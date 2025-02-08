var cluster = require('cluster');
var rx = require('bindings')('randomxhash.node');

var reverseBuffer = function (buff) {
    var reversed = Buffer.alloc(buff.length);
    for (var i = buff.length - 1; i >= 0; i--)
        reversed[buff.length - i - 1] = buff[i];
    return reversed;
};

var reverseHex = function (hex) {
    return reverseBuffer(Buffer.from(hex, 'hex')).toString('hex');
};

var numWorkers = require('os').cpus().length;
numWorkers = 1; /* increase for multi-thread testing */

if (cluster.isMaster) {
    var workers = [];
    var completedWorkers = 0; // Счётчик завершённых рабочих процессов

    for (var i = 0; i < numWorkers; i++) {
        var worker = cluster.fork({
            workerType: 'RandomXHasher',
            forkId: i
        });
        workers.push(worker);

        worker.on('exit', function (code, signal) {
            completedWorkers++;
            if (completedWorkers === numWorkers) {
                console.log('Все рабочие процессы завершены');
                process.exit(); // Завершаем главный процесс
            }
        });
    }
} else {
    rx.init(); // Инициализируем RandomX перед вычислением

    var input = Buffer.from('Test1234Test1234Test1234Test1234Test1234Test1234Test1234Test1234Test1234Test1234Test1234Test1234', 'utf8');

    var output = rx.hash(input);
    console.log(process.pid, 'RandomX Output', reverseHex(output.toString('hex')), '\n');

    rx.cleanup(); // Очищаем ресурсы RandomX после завершения

    process.exit(); // Завершаем рабочий процесс
}
