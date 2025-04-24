import React, { useState } from "react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

export default function ProductSearchLinkGenerator() {
const [product, setProduct] = useState("");
const [link, setLink] = useState("");

const generateLink = () => {
const query = encodeURIComponent(product);
const searchLink = https://www.google.com/search?q=${query};
setLink(searchLink);
};

return (




Генератор ссылки на продукт

<Input
type="text"
placeholder="Введите название продукта"
value={product}
onChange={(e) => setProduct(e.target.value)}
/>
Сгенерировать ссылку
{link && (


Перейти к результатам поиска


)}



);
}
