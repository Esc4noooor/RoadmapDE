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
## Вопросы по ClickHouse.

1. Принцип работы ClickHouse?
2. Какие основные движки ClickHouse ты знаешь?
3. Что такое гранулярность?
4. В чем различие primary key и order by при создании таблицы?
5. Где хранится индекс?
6. Что такое кардинальность и как она аффектит ключ распределения?
7. Что такое партиции и как они совмещены с primary key?
8. Как сделать таблицу распределённой в кластере?
9. Принцип работы MergeTree движков, и как хранятся данные?
10. Какие проблемы есть у движка ReplacingMergeTree?
11. Как в Clickhouse устроена операция UPDATE?
12. Какие индексы используются в ClickHouse?
13. Как работают JOIN в ClickHouse? 
14. Как в ClickHouse распределяются таблицы между шардами?
15. Какая машина является координатором в распределённом ClickHouse?
16. Какими свойствами САР-теоремы обладает ClickHouse?
17. Почему в ClickHouse нет JOIN по неравенству?
18. В каком случае ClickHouse выберит физический вид MergeJOIN?
19. Как PSQL сортирует данные при MergeJOIN , и почему так нельзя сделать в ClickHouse?
