PGDMP      (            	    |           empresa    16.4    16.4     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    32844    empresa    DATABASE     �   CREATE DATABASE empresa WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE empresa;
                postgres    false            �            1259    32860    arriendo    TABLE        CREATE TABLE public.arriendo (
    folio numeric(12,0) NOT NULL,
    fecha date,
    dias numeric(5,0),
    valor_dia numeric(12,0),
    garantia character varying(30),
    herramienta_id_herramienta numeric(12,0),
    cliente_rut character varying(10)
);
    DROP TABLE public.arriendo;
       public         heap    postgres    false            �            1259    32855    cliente    TABLE     �   CREATE TABLE public.cliente (
    rut character varying(10) NOT NULL,
    nombre character varying(120),
    direccion character varying(120),
    telefono character varying(15),
    correo character varying(80),
    web character varying(50)
);
    DROP TABLE public.cliente;
       public         heap    postgres    false            �            1259    32845    empresa    TABLE     �   CREATE TABLE public.empresa (
    rut character varying(10) NOT NULL,
    nombre character varying(120),
    "dirección" character varying(120),
    telefono character varying(15),
    correo character varying(80),
    web character varying(50)
);
    DROP TABLE public.empresa;
       public         heap    postgres    false            �            1259    32850    herramienta    TABLE     �   CREATE TABLE public.herramienta (
    id_herramienta numeric(12,0) NOT NULL,
    nombre character varying(120),
    precio_dia numeric(12,0)
);
    DROP TABLE public.herramienta;
       public         heap    postgres    false            �          0    32860    arriendo 
   TABLE DATA           t   COPY public.arriendo (folio, fecha, dias, valor_dia, garantia, herramienta_id_herramienta, cliente_rut) FROM stdin;
    public          postgres    false    218   �       �          0    32855    cliente 
   TABLE DATA           P   COPY public.cliente (rut, nombre, direccion, telefono, correo, web) FROM stdin;
    public          postgres    false    217   �       �          0    32845    empresa 
   TABLE DATA           S   COPY public.empresa (rut, nombre, "dirección", telefono, correo, web) FROM stdin;
    public          postgres    false    215   �       �          0    32850    herramienta 
   TABLE DATA           I   COPY public.herramienta (id_herramienta, nombre, precio_dia) FROM stdin;
    public          postgres    false    216          ,           2606    32864    arriendo arriendo_pk 
   CONSTRAINT     U   ALTER TABLE ONLY public.arriendo
    ADD CONSTRAINT arriendo_pk PRIMARY KEY (folio);
 >   ALTER TABLE ONLY public.arriendo DROP CONSTRAINT arriendo_pk;
       public            postgres    false    218            *           2606    32859    cliente cliente_pk 
   CONSTRAINT     Q   ALTER TABLE ONLY public.cliente
    ADD CONSTRAINT cliente_pk PRIMARY KEY (rut);
 <   ALTER TABLE ONLY public.cliente DROP CONSTRAINT cliente_pk;
       public            postgres    false    217            &           2606    32849    empresa empresa_pk 
   CONSTRAINT     Q   ALTER TABLE ONLY public.empresa
    ADD CONSTRAINT empresa_pk PRIMARY KEY (rut);
 <   ALTER TABLE ONLY public.empresa DROP CONSTRAINT empresa_pk;
       public            postgres    false    215            (           2606    32854    herramienta herramienta_pk 
   CONSTRAINT     d   ALTER TABLE ONLY public.herramienta
    ADD CONSTRAINT herramienta_pk PRIMARY KEY (id_herramienta);
 D   ALTER TABLE ONLY public.herramienta DROP CONSTRAINT herramienta_pk;
       public            postgres    false    216            -           2606    32870    arriendo arriendo_cliente_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.arriendo
    ADD CONSTRAINT arriendo_cliente_fk FOREIGN KEY (cliente_rut) REFERENCES public.cliente(rut);
 F   ALTER TABLE ONLY public.arriendo DROP CONSTRAINT arriendo_cliente_fk;
       public          postgres    false    218    4650    217            .           2606    32865     arriendo arriendo_herramienta_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.arriendo
    ADD CONSTRAINT arriendo_herramienta_fk FOREIGN KEY (herramienta_id_herramienta) REFERENCES public.herramienta(id_herramienta);
 J   ALTER TABLE ONLY public.arriendo DROP CONSTRAINT arriendo_herramienta_fk;
       public          postgres    false    4648    216    218            �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �     