<!-- Yandex.Metrika counter -->
<script type="text/javascript">
    (function(m,e,t,r,i,k,a){
        m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
        m[i].l=1*new Date();
        for (var j = 0; j < document.scripts.length; j++) {if (document.scripts[j].src === r) { return; }}
        k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)
    })(window, document,'script','https://mc.yandex.ru/metrika/tag.js?id=103580753', 'ym');

    ym(103580753, 'init', {ssr:true, webvisor:true, clickmap:true, ecommerce:"dataLayer", accurateTrackBounce:true, trackLinks:true});
</script>
<noscript><div><img src="https://mc.yandex.ru/watch/103580753" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
<!-- /Yandex.Metrika counter -->
# Clickhouse Cluster

Кластер Clickhouse был честно спизжен с данного ресурса, ибо нахер придумывать велосипед когда и так всё хорошо работает

## Запуск

Установите пакет **make** и перейдите в каталог с кластером.

```sh
sudo apt install make
```

Для поднятия всего кластера необходимо выполнить одну единственную команду:

```sh
make config up
```

В итоге поднимится кластер с именем `company_cluster`.

Контейнер находится в сети `172.23.0.0/24` (эта инфа нужна если вы делаете пет-проект и вы разграничиваете сети)

| Container    | Address
| ------------ | -------
| zookeeper    | 172.23.0.10
| clickhouse01 | 172.23.0.11
| clickhouse02 | 172.23.0.12
| clickhouse03 | 172.23.0.13
| clickhouse04 | 172.23.0.14

## Профиля

- `default` - no password
- `admin` - password `123`

## Старт и останвка

Старт и остановка контейнерос
```sh
make start
make stop
```

## Полная остановка

Полная остановка с удалением контейнера
```sh
make down
```
## Дополнительная конфигурация

Полазте по проекту, там нет абсолютно ничего сложного. Если захотите настройте его под себя.