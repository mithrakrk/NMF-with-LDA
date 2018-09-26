SELECT TOP 50000 post.*, postTag.Tag
FROM 
(
  SELECT Id, PostTypeId, Body, Title, Score, CreationDate
  FROM Posts
  WHERE PostTypeId = 1
    AND CreationDate BETWEEN '2017-01-01' AND '2017-12-31'
)AS post
INNER JOIN
(
  SELECT ptag.PostId as PostId, tag.TagName as Tag
  FROM PostTags AS ptag
  INNER JOIN Tags as tag
    ON tag.Id = ptag.TagId
    AND tag.TagName = 'python'
  GROUP BY ptag.PostID, tag.TagName
) AS postTag
ON post.Id = postTag.PostId
ORDER BY post.Score;
