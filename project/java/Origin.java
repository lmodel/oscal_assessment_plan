package None;

/* metamodel_version: 1.7.0 */
/* version: 1.2.1 */
import java.util.List;
import lombok.*;

/**
  Identifies the source of the finding, such as a tool, interviewed person, or activity.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Origin  {

  private List<OriginActor> actors;
  private List<RelatedTask> related-tasks;

}