
AWS İle Sunucusuz CRUD API Projesi
Giriş
Günümüzde web ve mobil uygulamalar, veri yönetimi için genellikle CRUD (Create, Read, Update, Delete) işlemlerine ihtiyaç duyarlar. Bu makalede, Amazon Web Services (AWS) kullanarak sunucusuz bir CRUD API'nin nasıl oluşturulacağını inceleyeceğiz. Bu proje, AWS Lambda, Amazon API Gateway ve Amazon DynamoDB (veya RDS) kullanılarak oluşturulacaktır.

Projenin Amacı
Bu projenin amacı, ölçeklenebilir, güvenilir ve bakım gerektirmeyen bir veri yönetim çözümü sunmaktır. AWS'nin sunduğu sunucusuz mimari, operasyonel maliyetleri düşürür ve geliştiricilerin altyapı yönetimi ile uğraşmadan uygulama geliştirmesine olanak tanır.

Kullanılan AWS Hizmetleri
AWS Lambda
AWS Lambda, sunucusuz mimariyi destekleyen bir hizmettir. Lambda ile sunucu yönetimi yapmadan kod çalıştırabilirsiniz. Bu proje kapsamında Lambda fonksiyonları, CRUD işlemlerini gerçekleştirmek için kullanılacaktır.

Amazon API Gateway
API Gateway, HTTP isteklerini Lambda fonksiyonlarına yönlendiren bir hizmettir. Bu, RESTful API'lerin kolayca oluşturulmasını sağlar ve API'lerin yönetimini basitleştirir.

Amazon DynamoDB ve Amazon RDS
DynamoDB: NoSQL veritabanı hizmeti olup, hızlı ve ölçeklenebilir veri depolama sağlar.
RDS: İlişkisel veritabanı hizmeti olup, PostgreSQL veya MySQL gibi veritabanlarını destekler.
