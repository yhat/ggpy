ggplot
======

What is it?
~~~~~~~~~~~

``ggplot`` is the Python version of the grammar of graphics. It is not
intended to be a feature-for-feature port of
```ggplot2 for R`` <https://github.com/hadley/ggplot2>`__. There is much
greatness in ``ggplot2``, the Python world could stand to benefit from
it.

What happened to the old version that didn't work?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It's gone--the windows, the doors,
`everything <https://www.youtube.com/watch?v=YuxCKv_0GZc>`__. I deleted
most of the code and only kept what worked. The data grouping and
manipulation bits were re-written (so they actually worked) with things
like facets in mind.

Where did ``stat_identity`` and ``geom_raster`` go?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

They're gone. They didn't even come close to working (also what does
``stat_identity`` even do) so they're gone.

.. code:: bash

    $ pip install https://github.com/yhat/ggplot/archive/overhaul.zip

Examples
~~~~~~~~

|image0| |image1| |image2| |image3| |image4| |image5| |image6| |image7|
|image8| |image9| |image10| |image11| |image12| |image13| |image14|
|image15| |image16| |image17| |image18| |image19| |image20| |image21|
|image22| |image23| |image24| |image25| |image26| |image27| |image28|
|image29| |image30| |image31| |image32| |image33| |image34| |image35|
|image36| |image37| |image38| |image39| |image40| |image41| |image42|
|image43| |image44| |image45| |image46| |image47| |image48| |image49|
|image50| |image51| |image52| |image53| |image54| |image55| |image56|
|image57| |image58| |image59| |image60| |image61| |image62| |image63|
|image64| |image65| |image66| |image67| |image68| |image69| |image70|
|image71| |image72| |image73| |image74| |image75| |image76| |image77|
|image78| |image79|

.. |image0| image:: ./examples/example-01ab6e56-bc32-455e-9842-45262fd341ad.png
.. |image1| image:: ./examples/example-02687ac6-7e68-4b28-9811-4ef487b20ba4.png
.. |image2| image:: ./examples/example-0514c0ae-944a-40e6-80cb-c037bc6a619d.png
.. |image3| image:: ./examples/example-0c9b8b58-fae4-447d-a78b-7913194cb1c8.png
.. |image4| image:: ./examples/example-0e43ff98-aefd-44e4-9e30-02c9ccf13e90.png
.. |image5| image:: ./examples/example-17bc1730-b20e-4d0c-a0ca-e40b517e82a3.png
.. |image6| image:: ./examples/example-1c3fbee1-1745-4570-9a00-56efba3085c4.png
.. |image7| image:: ./examples/example-1fbb7ef1-d295-464c-9234-38b54bb61e3d.png
.. |image8| image:: ./examples/example-20ab89e2-7ab6-417d-bba7-148fb92a8e30.png
.. |image9| image:: ./examples/example-20c9a55c-a526-4e85-af6b-8df86f466048.png
.. |image10| image:: ./examples/example-21469f96-98ce-4ca1-b1df-2306308f8e4b.png
.. |image11| image:: ./examples/example-21dedf76-0d4e-4074-b169-be7303e71dc1.png
.. |image12| image:: ./examples/example-2217f545-17d4-44b6-8a2f-1361ea310c10.png
.. |image13| image:: ./examples/example-2305e12b-23aa-4f41-bcd3-17d8a971eec8.png
.. |image14| image:: ./examples/example-2d2ad075-79fe-4fff-bda0-b520b5804e8d.png
.. |image15| image:: ./examples/example-311c7460-034d-48fc-ae71-d041c97663ef.png
.. |image16| image:: ./examples/example-3325f55f-fb4b-4a29-a105-8fa5cc3e6140.png
.. |image17| image:: ./examples/example-33cc1744-b9a7-4e2f-839a-73cc17dd11c3.png
.. |image18| image:: ./examples/example-34691ced-fae4-44a5-9f4e-cc33232143b3.png
.. |image19| image:: ./examples/example-34d773b9-ec68-40b1-999b-7bb07c208be9.png
.. |image20| image:: ./examples/example-3708e145-8f1b-485e-8c30-3241861c9177.png
.. |image21| image:: ./examples/example-44a1d142-63dc-4e73-9116-0b3c44ff9f33.png
.. |image22| image:: ./examples/example-48d8985c-a028-49c4-8c4b-b7d0dd335293.png
.. |image23| image:: ./examples/example-4a07a92f-f60c-4200-ba95-3e74dade461b.png
.. |image24| image:: ./examples/example-4b291adb-5c6b-4a59-b494-43123aa39d3e.png
.. |image25| image:: ./examples/example-4d23081c-e280-4664-b53d-a0f2e99f8479.png
.. |image26| image:: ./examples/example-4e6211d3-7d99-49ef-9c1a-d00887add29b.png
.. |image27| image:: ./examples/example-52ec20bb-446b-481e-a863-c65e40901446.png
.. |image28| image:: ./examples/example-55b23c7f-b847-446d-80ff-0d613781190e.png
.. |image29| image:: ./examples/example-5873a00c-ff47-4ab1-abe3-df8cc498c773.png
.. |image30| image:: ./examples/example-58c02486-17c6-48f2-b435-acf8da63d12d.png
.. |image31| image:: ./examples/example-5a7cbe1b-49ac-48a0-b3bc-15c2ad9183c5.png
.. |image32| image:: ./examples/example-5b540976-f321-43fa-bcc4-4d147031bc1a.png
.. |image33| image:: ./examples/example-5dddf73e-92e0-409d-9a95-f863b2c33d82.png
.. |image34| image:: ./examples/example-5f144c4e-33f3-44b5-b418-eaff8ada2054.png
.. |image35| image:: ./examples/example-648372f0-df2e-49e4-a5ef-cb0e1b0a1933.png
.. |image36| image:: ./examples/example-64b7425d-136f-48bd-a044-3e8cf869eea9.png
.. |image37| image:: ./examples/example-6fc05099-0330-4151-bc2c-0f18a28f7730.png
.. |image38| image:: ./examples/example-718416d1-895b-4883-8a30-ded4525e1719.png
.. |image39| image:: ./examples/example-7659cb36-63c9-4760-90e4-eece63890a67.png
.. |image40| image:: ./examples/example-76b48b01-1b41-4bf9-9880-a98acee7113c.png
.. |image41| image:: ./examples/example-811d20c0-2e38-4f59-979a-eb86e0b28e96.png
.. |image42| image:: ./examples/example-8f4fbffe-2999-42b0-9c34-de6f0b205733.png
.. |image43| image:: ./examples/example-8fccad7a-020c-4018-b7b1-569d73bdec89.png
.. |image44| image:: ./examples/example-904401f7-bc70-44f2-9440-845326905ed8.png
.. |image45| image:: ./examples/example-91784097-6377-4302-b9e1-b6735a01a235.png
.. |image46| image:: ./examples/example-96057f1a-6090-41f7-8d1a-129d6fdb78be.png
.. |image47| image:: ./examples/example-a0610ead-f774-4be3-a876-431442e086b6.png
.. |image48| image:: ./examples/example-a1e27e56-60f3-4d1e-9024-6b11e177a33c.png
.. |image49| image:: ./examples/example-a2af229a-ee7d-49a0-b163-a1e129570096.png
.. |image50| image:: ./examples/example-a3c87a12-0d9b-4747-8c2c-0ff6fe3e3cc5.png
.. |image51| image:: ./examples/example-a42c09e5-9977-4dbf-a9f6-32a1ced8b1d5.png
.. |image52| image:: ./examples/example-a5d47561-773c-49f8-b76a-91beaf1ecbb2.png
.. |image53| image:: ./examples/example-a7cf1dd8-104e-419c-90c7-ec0e5a5d10d7.png
.. |image54| image:: ./examples/example-a864af7f-458c-4017-b8c2-298d43afce77.png
.. |image55| image:: ./examples/example-aa977288-9cca-45d1-b743-c6e49b814cd7.png
.. |image56| image:: ./examples/example-ac1e1301-535f-4e59-91fa-d4c20d4fd23d.png
.. |image57| image:: ./examples/example-ad142339-1827-465e-86b0-478bcb5edbd4.png
.. |image58| image:: ./examples/example-b03399cc-ce45-44a9-b701-23f91c57a6cf.png
.. |image59| image:: ./examples/example-b2ed9041-ba23-470c-b10a-a461e6c0fa79.png
.. |image60| image:: ./examples/example-b4119243-8530-4429-9e93-ced574b2ce05.png
.. |image61| image:: ./examples/example-b86fdc16-ecb3-4b6a-b22e-386af6601b15.png
.. |image62| image:: ./examples/example-be8292ab-13dd-4192-8c0e-5ecb95e90cf6.png
.. |image63| image:: ./examples/example-c1ea42e5-435b-4e5e-9f2c-95bbe85e25d5.png
.. |image64| image:: ./examples/example-c5500838-014d-4fe3-809b-314cbf214d98.png
.. |image65| image:: ./examples/example-c600700b-d3b1-4fea-82cc-cd9d3582c93b.png
.. |image66| image:: ./examples/example-c6f0adff-ae6c-4c71-976e-a893be58c81f.png
.. |image67| image:: ./examples/example-c7c0a380-f50b-413a-beeb-b006e5740363.png
.. |image68| image:: ./examples/example-c9358e27-5145-447d-b31d-5ce6126cb1c1.png
.. |image69| image:: ./examples/example-c9c55564-02d9-4e5d-ba24-0ff411944aec.png
.. |image70| image:: ./examples/example-cd2bd612-e802-4910-924a-b7d77d3b9735.png
.. |image71| image:: ./examples/example-cd64f522-058b-49f0-a535-8401016fcfd4.png
.. |image72| image:: ./examples/example-d44c50b7-4cd5-4cd1-b901-e28dd4e25686.png
.. |image73| image:: ./examples/example-d951516d-6083-4b4f-b882-913f7024e9c5.png
.. |image74| image:: ./examples/example-dd48ccf1-f982-4fa5-9f92-065dcc44372e.png
.. |image75| image:: ./examples/example-dddae5d3-9714-4dd5-9c01-e674eafe18de.png
.. |image76| image:: ./examples/example-e38514e1-2aaa-4893-ba56-62b767649a74.png
.. |image77| image:: ./examples/example-ee62897e-f7c4-49c4-825e-9d8176fa32ed.png
.. |image78| image:: ./examples/example-f8aa92cf-1910-4c40-b11f-bb8079d4ccd8.png
.. |image79| image:: ./examples/example-fe1a8632-640a-470d-9a9a-1bdc3477fca3.png
